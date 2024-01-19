-- creates a table
-- create a table with a field with uniwue values
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR
);
