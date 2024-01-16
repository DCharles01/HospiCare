CREATE SCHEMA test_schema;
SET search_path TO test_schema, public;
SELECT test_create_tables('admissions');
DROP SCHEMA test_schema;
SET search_path TO public;

