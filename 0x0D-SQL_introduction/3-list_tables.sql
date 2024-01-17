-- listing all tables
-- lists all tables in a mysql server
SELECT table_schema, table_name
FROM information_schema.tables
ORDER BY table_schema, table_name;
