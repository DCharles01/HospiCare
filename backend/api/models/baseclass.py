from db.db_utils import *
from db.custom_errors import *

class BaseClass:
    __table__ = None
    columns = None
    # selected_keys = []

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.columns:
                raise ColNotInModel(f'Error: {key} not in {self.columns}')
            
        for key, value in kwargs.items():
            setattr(self, key, value)
            # self.selected_keys.append(key)

    @classmethod
    def find_all(cls, conn):
        cursor = conn.cursor()
        # breakpoint()
        cursor.execute(f'select * from {cls.__table__}')
        records = cursor.fetchall()
        return records
    
    @classmethod
    def find_by_id(cls, id, conn):
        cursor = conn.cursor()
        cursor.execute(f'select * from {cls.__table__} where id = %s', (id,))
        record = cursor.fetchone()

        return record

    @classmethod
    def get_latest_record(cls, conn):
        cursor = conn.cursor()
        select_query = f"""
        with latest_record as (
        SELECT 
        row_number() over () as row_num
        , *
        , count(*) over () as num_records
        FROM 
        {cls.__table__}
        )

        select * from latest_record where row_num = num_records
        
        """
    
        cursor.execute(select_query)
        record = cursor.fetchone()

        return build_from_record(cls, record)
    



