import psycopg2
from config_parser import load_config
def connect():
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            print('Connected to the PostgreSQL server.')
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
        return None
def insert_data(query, data):
    conn = connect()
    if conn:
        try:
            with conn.cursor() as cur:
                cur.execute(query, data)
                conn.commit()
                print("Data has been inserted successfully.")
        except (psycopg2.DatabaseError, Exception) as error:
            print(f"Error occurred during insert: {error}")
            conn.rollback()
        finally:
            conn.close()
            print("Connection closed.")
# query = "INSERT INTO your_table (column1, column2) VALUES (%s, %s)"
# data = ('value1', 'value2')
# insert_data(query, data)
import uuid
if __name__ == '__main__':
#Заполняем данные по периоду
    query = """
        INSERT INTO "periods" (
        "period_type_guid",
        "period_name"
        )
        VALUES (%s, %s);    
    """
    periods_ = ("day", "month", "quarter", "year")
    for period in periods_:
        random_uuid = str(uuid.uuid4())
        data = (random_uuid, period)
        insert_data(query, data)
    # query = """
    #     INSERT INTO "commercial_data" (
    #     "_guid", 
    #     "c_date", 
    #     "period_type_guid", 
    #     "asset_guid", 
    #     "well_guid", 
    #     "_location", 
    #     "fluid_guid", 
    #     "_value", 
    #     "unit_guid", 
    #     "license", 
    #     "info_type_guid"
    #     ) 
    #     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    # """
    # data = (
    #     'test-guid-001',    # _guid
    #     '2024-09-18',       # c_date
    #     'period-guid-001',  # period_type_guid
    #     'asset-guid-001',   # asset_guid
    #     'well-guid-001',    # well_guid
    #     'Test Location',    # _location
    #     'fluid-guid-001',   # fluid_guid
    #     100.5,              # _value
    #     'unit-guid-001',    # unit_guid
    #     'Test License',     # license
    #     'info-guid-001'     # info_type_guid
    # )
    # insert_data(query, data)
