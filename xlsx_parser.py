import pandas as pd


names = [
    'project',
    
    'date',
    
    'gas_production_value_m3',

    'gas_consume_burned_m3',
    'gas_consume_fuel_m3',
    'gas_consume_converted_m3',
    
    'gas_commercial_value_m3',
    'gas_commercial_plan_daily_m3',
    'gas_commercial_plan_nomintaion_m3',
    
    'condensat_production_value_m3',
    'condensat_production_weight_t',
    'condensat_commercial_value_m3',
    'condensat_commercial_weight_t',

    'pbf_production_value_m3',
    'pbf_commercial_value_m3',

    'gasoline_production_value_m3',
    'gasoline_commercial_value_m3',

    'oil_production_value_m3',
    'oil_production_weight_t',
    'oil_commercial_value_m3',
    'oil_commercial_weight_t',
    'oil_commercial_plan_daily_t',

    'water_production_m3',
    'water_injection_m3'
    'water_util_m3',
    
    'presure_in_atm',
    'presure_out_atm',

    'found_total',
    'found_active',
    'found_daily_work',

    'comment'
]

commercial_names = [
    'project',
    
    'date',

    'gas_commercial_value_m3',
    'gas_commercial_plan_daily_m3',
    'gas_commercial_plan_nomintaion_m3',
    
    'condensat_commercial_value_m3',
    'condensat_commercial_weight_t',

    'pbf_commercial_value_m3',

    'gasoline_commercial_value_m3',
    
    'water_production_m3',
    'water_injection_m3'
    'water_util_m3',

    'oil_commercial_value_m3',
    'oil_commercial_weight_t',
    'oil_commercial_plan_daily_t',
    
    'found_total',
    'found_active',
    'found_daily_work',

    'comment'
]

#parsed all
# data = pd.read_excel(
#         'project_data.xlsx',
#         names=names,
#         header=None,
#         skiprows=3,
#         # nrows=10,
#         index_col=False
#     )
# # print(data)
# data.to_csv('temp_files\\all_data_from_table.csv', index=False)

# #only commercial
# only_commercial_data = data[commercial_names]
# only_commercial_data.to_csv('temp_files\\commercial_data_from_table.csv', index=False)




df = pd.read_csv('temp_files\\commercial_data_from_table.csv',
                nrows=10
                )
print(df)
