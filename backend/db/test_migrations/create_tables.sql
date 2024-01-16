-- Function to test the create_tables function
CREATE OR REPLACE FUNCTION test_create_tables(table_name text)
RETURNS VOID AS $$
DECLARE
    table_exists BOOLEAN;
    index_exists BOOLEAN;
BEGIN
    -- Execute the function to create tables
    PERFORM test_schema.create_tables();

    -- Test if the 'patients' table exists
    SELECT EXISTS (
        SELECT 1
        FROM information_schema.tables
        -- this table is the key to most tables
        WHERE table_name = table_name
          AND table_schema = 'test_schema'
    ) INTO table_exists;

    ASSERT table_exists = TRUE, format('%s table not created', table_name);

    -- Test if the 'idx_admissions_id' index exists
    SELECT EXISTS (
        SELECT 1
        FROM pg_indexes
        WHERE indexname = 'idx_admissions_id'
          AND schemaname = 'test_schema'
    ) INTO index_exists;

    ASSERT index_exists = TRUE, 'Index idx_admissions_id not created';
END;
$$ LANGUAGE plpgsql;

