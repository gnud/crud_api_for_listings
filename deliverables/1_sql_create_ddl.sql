BEGIN;
--
-- Create model Listing
--
CREATE TABLE "realestate_listing"
(
    "id"               integer      NOT NULL PRIMARY KEY AUTOINCREMENT,
    "property_address" varchar(255) NOT NULL,
    "listing_price"    integer      NOT NULL
);
COMMIT;
