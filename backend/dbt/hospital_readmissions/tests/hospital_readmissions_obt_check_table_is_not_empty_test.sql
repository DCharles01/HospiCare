-- Test: Result should not be empty
SELECT status, FROM {{ ref('hospital_readmissions_obt') }} where status is null;
-- -- Expectation: No null values in my_column
-- SELECT row_count FROM {{ ref('hospital_readmissions_obt_check_table_is_not_empty_test') }} WHERE row_count > 0;