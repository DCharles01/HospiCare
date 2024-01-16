CREATE OR REPLACE FUNCTION get_constraints_in_schema(schema_name text, input_table_name text)
RETURNS TABLE (
    constraint_name text,
    constraint_type text,
    table_name regclass,
    column_name text,
    referenced_table_name regclass,
    referenced_column_name text
) AS $$
BEGIN
    RETURN QUERY
    SELECT
        con.conname::text AS constraint_name,
        CASE
            WHEN con.contype = 'p' THEN 'PRIMARY KEY'
            WHEN con.contype = 'u' THEN 'UNIQUE'
            WHEN con.contype = 'c' THEN 'CHECK'
            WHEN con.contype = 'f' THEN 'FOREIGN KEY'
            ELSE 'UNKNOWN'
        END::text AS constraint_type,
        rel.relname::regclass AS table_name,
        att.attname::text AS column_name,
        ref.relname::regclass AS referenced_table_name,
        ref_att.attname::text AS referenced_column_name
    FROM
        pg_catalog.pg_constraint con
    INNER JOIN
        pg_catalog.pg_class rel ON rel.oid = con.conrelid
    INNER JOIN
        pg_catalog.pg_namespace nsp ON nsp.oid = connamespace
    INNER JOIN
        pg_catalog.pg_attribute att ON att.attnum = ANY(con.conkey) AND att.attrelid = con.conrelid
    LEFT JOIN
        pg_catalog.pg_class ref ON ref.oid = con.confrelid
    LEFT JOIN
        pg_catalog.pg_attribute ref_att ON ref_att.attnum = ANY(con.confkey) AND ref_att.attrelid = con.confrelid
    WHERE
        nsp.nspname = schema_name
        AND rel.relname = input_table_name;

END;
$$ LANGUAGE plpgsql;
