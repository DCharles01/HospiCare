import psycopg2
from settings import DB_USER, TEST_DB_USER, DB_PASSWORD, DB_HOST, DB_NAME, TEST_DB_NAME
from .custom_errors import DBNameNotTest

test_conn = psycopg2.connect(user=TEST_DB_USER, 
                             password=DB_PASSWORD,
                             dbname=TEST_DB_NAME,
                             host=DB_HOST)

test_cursor = test_conn.cursor()
# breakpoint()
prod_conn = psycopg2.connect(user=DB_USER, 
                             password=DB_PASSWORD,
                             dbname=DB_NAME,
                             host=DB_HOST)

# custom ORM methods
def build_from_record(Class, record):
    if not record: return None
    # breakpoint()
    # create dict from db record
    attrs = dict(zip(Class.columns, record))

    # create new class instance
    obj = Class()

    # set attrs dict to class.__dict__
    obj.__dict__ = attrs

    return obj

def build_from_records(Class, records):
    return [build_from_record(Class, record) for record in records]

def keys(Class):
    key_attr = [col for col in Class.columns if col in Class.__dict__.keys()]

    key_str = ','.join(key_attr)

    return key_str

def values(Class):
    val_dict = Class.__dict__
    val_attr = [val_dict[col] for col in Class.columns if col in val_dict.keys()]

    return val_attr
    

def save(Class, conn, cursor):
    # breakpoint()
    s_str = ', '.join(len(values(Class)) * ['%s'])
    # build insert query for Class instance
    insert_query = f"INSERT INTO {Class.__table__} ({keys(Class)}) VALUES ({s_str})"


    cursor = conn.cursor()

    # execute query
    cursor.execute(insert_query, list(values(Class)))

    # save changes to database
    conn.commit()

    # record = Class.get_latest_record(conn)

    cursor.execute(f'SELECT * FROM {Class.__table__} ORDER BY id DESC LIMIT 1')
    record = cursor.fetchone()
    return build_from_record(type(Class), record)

    # return build_from_record(type(Class), record)


def drop_all_tables(conn):
    cursor = conn.cursor()
    # breakpoint()
    if 'test' not in conn.get_dsn_parameters()['dbname']:
        raise DBNameNotTest(f"Error: {conn.get_dsn_parameters()['dbname']} is not a test database. Rolling back changes.")
    
    
    cursor.execute('select drop_all_tables()')
    conn.commit()

def create_all_tables(conn):
    cursor = conn.cursor()
    # breakpoint()
    if 'test' not in conn.get_dsn_parameters()['dbname']:
        raise DBNameNotTest(f"Error: {conn.get_dsn_parameters()['dbname']} is not a test database. Rolling back changes.")
    
    
    cursor.execute('select create_tables()')
    conn.commit()



