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


import numpy as np


df = pd.read_csv('temp_files\\all_data_from_table.csv')

df['date'] = pd.to_datetime(df['date'])

# fil_well_df =

#убрал date, будет наследоваться от основного dataframe
filtered_df = df[['project', 'date', 'gas_production_value_m3', 'gas_commercial_value_m3', 'gas_commercial_plan_daily_m3', 'gas_commercial_plan_nomintaion_m3']]

filtered_df = filtered_df[(df['date'].dt.year == 2021) & (df['date'].dt.month == 5)]

filtered_df['day'] = filtered_df['date'].dt.day


filtered_df['found_total'] = np.random.randint(15, 20, size=len(filtered_df))
filtered_df['found_active'] = [np.random.randint(10, total) for total in filtered_df['found_total']]
filtered_df['found_daily_work'] = [np.random.randint(8, active) for active in filtered_df['found_active']]

print(filtered_df)




df_melted = pd.melt(filtered_df, id_vars=['day'], value_vars=['gas_production_value_m3', 'gas_commercial_value_m3', 'gas_commercial_plan_daily_m3', 'gas_commercial_plan_nomintaion_m3'], 
                    var_name='type', value_name='value')


import plotly.graph_objects as go

from plotly.subplots import make_subplots

import plotly.express as px

def create_figure():
    fig = go.Figure()

    # Линии для добычи и плана
    fig.add_trace(go.Scatter(x=filtered_df['day'], y=filtered_df['gas_production_value_m3'], mode='lines', name='Факт на устье', yaxis='y1'))
    fig.add_trace(go.Scatter(x=filtered_df['day'], y=filtered_df['gas_commercial_value_m3'], mode='lines', name='Факт товарный', yaxis='y1'))
    fig.add_trace(go.Scatter(x=filtered_df['day'], y=filtered_df['gas_commercial_plan_daily_m3'], mode='lines', name='План суточный', yaxis='y1'))
    fig.add_trace(go.Scatter(x=filtered_df['day'], y=filtered_df['gas_commercial_plan_nomintaion_m3'], mode='lines', name='План номинация', yaxis='y1'))



    fig.add_trace(go.Bar(x=filtered_df['day'], y=filtered_df['found_total'], name='Фонд скважин', opacity=0.6, yaxis='y2'))
    fig.add_trace(go.Bar(x=filtered_df['day'], y=filtered_df['found_active'], name='Активные скважины', opacity=0.6, yaxis='y2'))
    fig.add_trace(go.Bar(x=filtered_df['day'], y=filtered_df['found_daily_work'], name='В добыче', opacity=0.6, yaxis='y2'))




    fig.update_layout(
        title='Комбинированный график: Добыча, План и Скважины',
        xaxis_title='Дата',
        yaxis_title='Объем',
        yaxis=dict(title='Объем', side='left'),  # Ось Y для добычи слева
        yaxis2=dict(title='Скважины', overlaying='y', side='right'),  # Ось Y для скважин справа
        barmode='overlay',  # Накладываем гистограммы друг на друга
        legend=dict(title='', orientation='h', x=0.5, y=-0.2, xanchor='center', yanchor='top', bgcolor='rgba(255, 255, 255, 0)'),
    )


    return fig


# import plotly.express as px
from dash import dcc, html

render_me = html.Div([
                html.H1("График добычи и плана"),
                dcc.Graph(id='line-chart', figure=create_figure())
            ])
