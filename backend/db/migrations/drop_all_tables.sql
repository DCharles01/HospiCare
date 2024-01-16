-- CREATE OR REPLACE FUNCTION drop_all_tables()
-- RETURNS VOID AS $$
-- DECLARE
--     v_table_name TEXT;
-- BEGIN
--     FOR v_table_name IN
--         SELECT table_name FROM information_schema.tables
--         WHERE table_schema = 'public' AND table_type = 'BASE TABLE'
--     LOOP
--         EXECUTE 'DROP TABLE IF EXISTS ' || v_table_name || ' CASCADE';
--     END LOOP;
-- END;
-- $$ LANGUAGE plpgsql;

-- 
CREATE OR REPLACE FUNCTION drop_all_tables()
RETURNS VOID AS $$
DECLARE
    v_table_name TEXT;
    v_db_name TEXT;
BEGIN
    -- Get the current database name
    SELECT current_database() INTO v_db_name;

    -- Check if the database name contains 'test'
    -- IF POSITION('test' IN v_db_name) = 0 THEN
    --     -- If 'test' is not detected, raise a notice, rollback changes, and end the query
    --     RAISE NOTICE 'Database % does not contain "test". Rolling back changes.', v_db_name;
    --     RETURN;
    -- END IF;

    -- If 'test' is detected in the database name, proceed with dropping tables
    FOR v_table_name IN
        SELECT table_name FROM information_schema.tables
        WHERE table_schema = 'public' AND table_type = 'BASE TABLE'
    LOOP
        -- -- Check if the table name contains 'test'
        -- IF POSITION('test' IN v_table_name) > 0 THEN
        --     -- If 'test' is detected in a table name, raise a notice and continue with the loop
        --     RAISE NOTICE 'Table % contains "test". Skipping this table.', v_table_name;
        -- ELSE
        --     -- If 'test' is not detected in the table name, proceed with dropping the table
        --     EXECUTE 'DROP TABLE IF EXISTS ' || v_table_name || ' CASCADE';
        -- END IF;

        EXECUTE 'DROP TABLE IF EXISTS ' || v_table_name || ' CASCADE';
        RAISE NOTICE 'Dropped table %.', v_table_name;
    END LOOP;
END;
$$ LANGUAGE plpgsql;
