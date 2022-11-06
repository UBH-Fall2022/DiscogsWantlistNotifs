SET sql_safe_updates = FALSE;

USE defaultdb;
DROP DATABASE IF EXISTS wantlist CASCADE;
CREATE DATABASE IF NOT EXISTS wantlist;

USE wantlist;

CREATE TABLE wantlist_data (
    id INT8,
    album STRING,
    artist STRING,
    format STRING,
    num_on_sale INT8,
    lowest_price FLOAT,
);

INSERT INTO wantlist_data (id, album, artist, format, num_on_sale, lowest_price)
  VALUES (2345, 'From Under The Cork Tree', 'Fall Out Boy', 'Vinyl', 100, 15.99);

