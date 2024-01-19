-- creating a table for a specific DB
-- create table states in db hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- uses the database hbtn_0d_usa
USE hbtn_0d_usa;
-- creates a table in database
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
