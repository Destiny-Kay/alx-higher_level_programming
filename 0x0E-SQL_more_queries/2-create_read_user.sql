-- creating a database and assigning privileges to a user
--creating a database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
--creating a user
CREATE USER IF NOT EXISTS 'user_0d_2@localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- granting select permission to user
GRANT SELECT  ON hbtn_0d_2 TO 'user_0d)2@localhost';
