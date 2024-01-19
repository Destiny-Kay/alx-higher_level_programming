-- creating a db and table
-- creating a database
CREATE DATABASE IF NOT EXISTS hbtn_od_usa;
-- using the db
USE hbtn_0d_usa;
-- creating a table
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
