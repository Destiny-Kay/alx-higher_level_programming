-- Creating and adding records in a DB
-- Creates database tables and adds records to it
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);
-- inserts records to the database
INSERT INTO second_table(id, name, score)
VALUES
    (1, "John", 10),
    (2, "Alex", 3),
    (3, "Bob", 14),
    (4, "George", 8)
;
