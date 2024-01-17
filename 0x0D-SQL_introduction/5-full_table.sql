-- prints a full description of a table
-- The query
SELECT COLUMN_NAME DATA_TYPE, IS_NULLABLE, COLUMN_DEFAULT
FROM information_schema.columns
WHERE TABLE_NAME = 'first_table';
