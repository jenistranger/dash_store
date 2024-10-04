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


# query = "INSERT INTO your_table (column1, column2) VALUES (%s, %s)"
# data = ('value1', 'value2')
# insert_data(query, data)
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


import uuid
def upd_reference_table(table_name, column1, column2, data):
    query = f"""
        INSERT INTO "{table_name}" (
        "{column1}",
        "{column2}"
        )
        VALUES (%s, %s);    
    """ 
    for item in data:
        random_uuid = str(uuid.uuid4())
        temp_data = (random_uuid, item)
        insert_data(query, temp_data)


def load_countries():
    conn = connect()
    if conn:
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT country_name FROM countries")
                record = cur.fetchall()
                
                return record
                
        except (psycopg2.DatabaseError, Exception) as error:
            print(f"Error occurred during insert: {error}")
            conn.rollback()
        finally:
            conn.close()
            print("Connection closed.")

def get_country_guid(target):
    conn = connect()
    if conn:
        try:
            with conn.cursor() as cur:
                cur.execute(f"SELECT country_guid FROM countries WHERE country_name = \'{target}\'")
                record = cur.fetchone()[0]
                return record
        except (psycopg2.DatabaseError, Exception) as error:
            print(f"Error occurred during insert: {error}")
            conn.rollback()
        finally:
            conn.close()
            print("Connection closed.")



if __name__ == '__main__':


    pass
    # assets_data = [
    #         (str(uuid.uuid4()), 'Актив 1', str(get_country_guid("Боливия")), 10),
    #         (str(uuid.uuid4()), 'Актив 2', str(get_country_guid("Вьетнам")), 15),
    #         (str(uuid.uuid4()), 'Актив 3', str(get_country_guid("Алжир")), 8)
    #     ]
    
    # for a_data in assets_data:
    #     query = ("INSERT INTO assets (asset_guid, asset_name, country_guid, total_wells) VALUES (%s, %s, %s, %s)")
    #     insert_data(query, a_data)
