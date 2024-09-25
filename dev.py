import random
from datetime import date, timedelta, datetime


from db_main import connect
import psycopg2


# if __name__ == "__main__":
#     for item in range(start, end):
#         print(item)


def daterange(start_date: date, end_date: date):
    days = int((end_date - start_date).days)
    for n in range(days+1):
        yield start_date + timedelta(n)


#одна страна
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

#все 
def get_country_guid():
    conn = connect()
    if conn:
        try:
            with conn.cursor() as cur:
                cur.execute(f"SELECT country_guid FROM countries;")
                record = cur.fetchall()
                countries_guid = []
                for item in record:
                    countries_guid.append(item[0])
                print(countries_guid)
                return countries_guid
        except (psycopg2.DatabaseError, Exception) as error:
            print(f"Error occurred during insert: {error}")
            conn.rollback()
        finally:
            conn.close()
            print("Connection closed.")

def set_country_guid():
    pass





#все
def get_asset_guid():
    conn = connect()
    if conn:
        try:
            with conn.cursor() as cur:
                cur.execute(f"SELECT asset_guid FROM assets;")
                record = cur.fetchall()
                assets_guid = []
                for item in record:
                    assets_guid.append(item[0])
                print(assets_guid)
                return assets_guid
        except (psycopg2.DatabaseError, Exception) as error:
            print(f"Error occurred during insert: {error}")
            conn.rollback()
        finally:
            conn.close()
            print("Connection closed.")

def set_asset_guid():
    pass

def get_period_guid(target):
    conn = connect()
    if conn:
        try:
            with conn.cursor() as cur:
                cur.execute(f"SELECT period_type_guid FROM periods WHERE period_name = \'{target}\'")
                record = cur.fetchone()[0]
                print(record)
                return record
        except (psycopg2.DatabaseError, Exception) as error:
            print(f"Error occurred during insert: {error}")
            conn.rollback()
        finally:
            conn.close()
            print("Connection closed.")

def set_period_guid():
    pass

def get_well_guid():
    pass


def set_well_guid():
    #дописать
    pass

def get_fluid_guid():
    conn = connect()
    if conn:
        try:
            with conn.cursor() as cur:
                cur.execute(f"SELECT fluid_guid FROM fluids;")
                record = cur.fetchall()
                fluids_guid = []
                for item in record:
                    fluids_guid.append(item[0])
                print(fluids_guid)
                return fluids_guid
        except (psycopg2.DatabaseError, Exception) as error:
            print(f"Error occurred during insert: {error}")
            conn.rollback()
        finally:
            conn.close()
            print("Connection closed.")

def set_fluid_guid():
    pass

def get_unit_guid():
    conn = connect()
    if conn:
        try:
            with conn.cursor() as cur:
                cur.execute(f"SELECT unit_guid FROM units;")
                record = cur.fetchall()
                units_guid = []
                for item in record:
                    units_guid.append(item[0])
                print(units_guid)
                return units_guid
        except (psycopg2.DatabaseError, Exception) as error:
            print(f"Error occurred during insert: {error}")
            conn.rollback()
        finally:
            conn.close()
            print("Connection closed.")

def get_unit_guid(target):
    conn = connect()
    if conn:
        try:
            with conn.cursor() as cur:
                cur.execute(f"SELECT unit_guid FROM units WHERE unit_name = \'{target}\'")
                record = cur.fetchone()[0]
                print(record)
                return record
        except (psycopg2.DatabaseError, Exception) as error:
            print(f"Error occurred during insert: {error}")
            conn.rollback()
        finally:
            conn.close()
            print("Connection closed.")

def set_unit_guid():
    pass

def get_info_guid():
    conn = connect()
    if conn:
        try:
            with conn.cursor() as cur:
                cur.execute(f"SELECT info_type_guid FROM infos;")
                record = cur.fetchall()
                info_types_guid = []
                for item in record:
                    info_types_guid.append(item[0])
                print(info_types_guid)
                return info_types_guid
        except (psycopg2.DatabaseError, Exception) as error:
            print(f"Error occurred during insert: {error}")
            conn.rollback()
        finally:
            conn.close()
            print("Connection closed.")

def set_info_guid():
    pass

def get_com_data():
    pass

def set_com_data(date):
    pass


import uuid

def daily_commercial_data(date, period, asset, fluid, value, unit, info):
    random_uuid = str(uuid.uuid4())
    conn = connect()
    if conn:
        try:
            with conn.cursor() as cur:
                cur.execute("""INSERT INTO commercial_data (_guid, c_date, period_type_guid, asset_guid, fluid_guid, _value, unit_guid, info_type_guid) 
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                            """, (random_uuid, date, period, asset, fluid, value, unit, info))
                conn.commit()
                print("Data has been inserted successfully.")
        except (psycopg2.DatabaseError, Exception) as error:
            print(f"Error occurred during insert: {error}")
            conn.rollback()
        finally:
            conn.close()
            print("Connection closed.")

def daily_wells_activity():
    pass


def month_commercial_data():
    pass

def quarter_commercial_data():
    pass

def year_commercial_data():
    pass

#для plan day
def get_plan_volume():

    pass

if __name__ == "__main__":
    start = date(2023, 5, 1)
    end = datetime.date(datetime.now())
    period = get_period_guid('day')
    unit_guid = get_unit_guid('mil_m3')
    list_of_assets = get_asset_guid()
    list_of_fluids = get_fluid_guid()
    list_of_infos = get_info_guid()
    for single_date in daterange(start, end):
        for asset in list_of_assets:
            for fluid in list_of_fluids:
                for info in list_of_infos:
                    value = round(random.uniform(100, 300), 1)
                    daily_commercial_data(single_date, period, asset, fluid, value, unit_guid, info)





    # print()


        # print(single_date)

        # print(f"{single_date.strftime('%d.%m.%Y')}") 

    # print(datetime.now())
    # get_country_guid()
    # get_asset_guid()
    # get_fluid_guid()
    # get_info_guid()

