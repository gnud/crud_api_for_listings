from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from faker import Faker

fake = Faker()

test_user = fake.name().lower().replace(' ', '')
test_password = 'Pas$w0rd'


def create_listing() -> dict[str, str]:
    random_address = fake.address()
    random_price = fake.random.randint(10000, 90000)

    data = {
        'property_address': random_address,
        'listing_price': random_price,
    }

    return data


class ListingTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        try:
            user = get_user_model().objects.create_user(
                username=test_user,
                password=test_password,
                email=fake.email(),
            )
        except Exception as e:
            pass

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.client = APIClient()

    def test_create_listing(self):
        data = create_listing()
        self.client.login(username=test_user, password=test_password)

        res = self.client.post('/listing/', data)
        self.assertEquals(res.status_code, status.HTTP_201_CREATED)

    def test_read_listing(self):
        data = create_listing()

        self.client.login(username=test_user, password=test_password)

        # prepare data
        res_create = self.client.post('/listing/', data)
        res_create_data = res_create.data
        res_pk = res_create_data.get('pk')

        res = self.client.get(f'/listing/{res_pk}/')

        self.assertEquals(res.status_code, status.HTTP_200_OK)

    def test_list_listing(self):
        data = create_listing()
        self.client.login(username=test_user, password=test_password)

        self.client.post('/listing/', data)

        res = self.client.get('/listing/')

        self.assertEquals(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)

    def test_update_listing(self):
        data = create_listing()

        # randomize the data to differ from the original data
        data_update = data.copy()
        data_update['property_address'] = fake.address()

        self.client.login(username=test_user, password=test_password)

        # prepare data
        res_create = self.client.post('/listing/', data)
        res_create_data = res_create.data
        res_pk = res_create_data.get('pk')

        res = self.client.put(f'/listing/{res_pk}/', data_update)
        res_data = res.data.copy()
        res_data.pop('pk')

        self.assertEquals(res.status_code, status.HTTP_200_OK)
        self.assertDictEqual(res_data, data_update)

    def test_delete_listing(self):
        data = create_listing()

        self.client.login(username=test_user, password=test_password)

        # prepare data
        res_create = self.client.post('/listing/', data)
        res_create_data = res_create.data
        res_pk = res_create_data.get('pk')

        res = self.client.delete(f'/listing/{res_pk}/')

        self.assertEquals(res.status_code, status.HTTP_204_NO_CONTENT)
