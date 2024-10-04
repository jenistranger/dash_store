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



#форма для работы с csv
# df = pd.read_csv('temp_files\\all_data_from_table.csv')

# df['date'] = pd.to_datetime(df['date'])

# filtered_df = df[['project', 'date', 'gas_production_value_m3', 'gas_commercial_value_m3', 'gas_commercial_plan_daily_m3', 'gas_commercial_plan_nomintaion_m3']]

# filtered_df = filtered_df[(df['date'].dt.year == 2017) & (df['date'].dt.month == 5)]

# filtered_df['day'] = filtered_df['date'].dt.day


# filtered_df['found_total'] = np.random.randint(15, 20, size=len(filtered_df))
# filtered_df['found_active'] = [np.random.randint(10, total) for total in filtered_df['found_total']]
# filtered_df['found_daily_work'] = [np.random.randint(8, active) for active in filtered_df['found_active']]

# # print(filtered_df)


# df_melted = pd.melt(filtered_df, id_vars=['day'], value_vars=['gas_production_value_m3', 'gas_commercial_value_m3', 'gas_commercial_plan_daily_m3', 'gas_commercial_plan_nomintaion_m3'], 
#                     var_name='type', value_name='value')


import plotly.graph_objects as go

from plotly.subplots import make_subplots

import plotly.express as px


#добавить отклонение
def create_fig_with_wells(month, year):
    df = pd.read_csv('temp_files\\all_data_from_table.csv')

    # df['date'] = pd.to_datetime(df['date'])
    df.loc[:, 'date'] = pd.to_datetime(df['date'])
    
    
    filtered_df = df[['project', 'date', 'gas_production_value_m3', 'gas_commercial_value_m3', 'gas_commercial_plan_daily_m3', 'gas_commercial_plan_nomintaion_m3']]
    year_to_check = year
    month_to_check = month


    filtered_df = filtered_df[(filtered_df['date'].dt.year == year_to_check) & (filtered_df['date'].dt.month == month_to_check)]
    # filtered_df = filtered_df[(df['date'].dt.year == year_to_check) & (df['date'].dt.month == month_to_check)]
    
    
    # filtered_df['day'] = filtered_df['date'].dt.day
    filtered_df.loc[:, 'day'] = filtered_df['date'].dt.day



    filtered_df['found_total'] = np.random.randint(15, 20, size=len(filtered_df))
    filtered_df['found_active'] = [np.random.randint(10, total) for total in filtered_df['found_total']]
    filtered_df['found_daily_work'] = [np.random.randint(8, active) for active in filtered_df['found_active']]

    # df_melted = pd.melt(filtered_df, id_vars=['day'], value_vars=['gas_production_value_m3', 'gas_commercial_value_m3', 'gas_commercial_plan_daily_m3', 'gas_commercial_plan_nomintaion_m3'], 
    #                     var_name='type', value_name='value')

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=filtered_df['day'], y=filtered_df['gas_production_value_m3'], mode='lines', name='Факт на устье', yaxis='y2', line=dict(color="darkblue")))
    fig.add_trace(go.Scatter(x=filtered_df['day'], y=filtered_df['gas_commercial_value_m3'], mode='lines', name='Факт товарный', yaxis='y2', line=dict(color=" royalblue")))
    fig.add_trace(go.Scatter(x=filtered_df['day'], y=filtered_df['gas_commercial_plan_daily_m3'], mode='lines', name='План суточный', yaxis='y2', line=dict(color="red", dash="dot", width=4,)))
    fig.add_trace(go.Scatter(x=filtered_df['day'], y=filtered_df['gas_commercial_plan_nomintaion_m3'], mode='lines', name='План номинация', yaxis='y2', line=dict(color="#6f32a8")))
    fig.add_trace(go.Bar(x=filtered_df['day'], y=filtered_df['found_total'], name='Фонд скважин', opacity=0.7, yaxis='y1', marker_color='#40a7ff', width=0.5))
    fig.add_trace(go.Bar(x=filtered_df['day'], y=filtered_df['found_daily_work'], name='В добыче', opacity=0.6, yaxis='y1', marker_color='#797979', width=0.5))
    fig.update_layout(
        title='Суточная добыча и поставка газа за ...',
        xaxis_title='Дата',
        yaxis_title='Объем',
        yaxis2=dict(
                title='м<sup>3</sup>', 
                overlaying='y', 
                side='left',
                # tickformat=".2s",
                # ticksuffix=""
            ), 
        yaxis=dict(title='Скважины', side='right' ),
        barmode='overlay',  # Накладываем гистограммы друг на друга
        legend=dict(title='', orientation='h', x=0.5, y=-0.2, xanchor='center', yanchor='top', bgcolor='rgba(255, 255, 255, 0)'),
        hovermode="x unified"
    )

    return fig




def create_fig_plus(year):
    month_vals = [
        'Январь',
        'Февраль',
        'Март',
        'Апрель',
        'Май',
        'Июнь',
        'Июль',
        'Август',
        'Сентябрь',
        'Октябрь',
        'Ноябрь',
        'Декабрь',
        
    ]
    
    df = pd.read_csv('temp_files\\all_data_from_table.csv')

    df = df[['project', 'date', 'gas_production_value_m3', 'gas_commercial_value_m3', 'gas_commercial_plan_daily_m3', 'gas_commercial_plan_nomintaion_m3']]



    # df['date'] = pd.to_datetime(df['date'])
    # df['month'] = df['date'].dt.month
    # df['year'] = df['date'].dt.year
    df.loc[:, 'date'] = pd.to_datetime(df['date'])
    df.loc[:, 'month'] = df['date'].dt.month
    df.loc[:, 'year'] = df['date'].dt.year

    

    # month_to_sum = 7
    # year_to_sum = 2021
    # filtred_df = df[df['month'] == month_to_sum]
    # filtred_df = df[(df['date'].dt.year == year_to_sum) & (df['date'].dt.month == month_to_sum)]
    # summed = filtred_df.sum(numeric_only=True)

    grouped_df = df.groupby(['year', 'month']).sum(numeric_only=True).reset_index()
    
    year_to_filter = year

    filtered_df = grouped_df[grouped_df['year'] == year_to_filter]


    # filtered_df['cumsum_gas_production'] = filtered_df['gas_production_value_m3'].cumsum()    
    # filtered_df['cumsum_gas_commercial_plan'] = filtered_df['gas_commercial_plan_daily_m3'].cumsum()
    # filtered_df['cumsum_gas_commercial_nomination'] = filtered_df['gas_commercial_plan_nomintaion_m3'].cumsum()
    filtered_df.loc[:, 'cumsum_gas_production'] = filtered_df['gas_production_value_m3'].cumsum()    
    filtered_df.loc[:, 'cumsum_gas_commercial_plan'] = filtered_df['gas_commercial_plan_daily_m3'].cumsum()
    filtered_df.loc[:, 'cumsum_gas_commercial_nomination'] = filtered_df['gas_commercial_plan_nomintaion_m3'].cumsum()

    fig = go.Figure()


    fig.add_trace(
        go.Scatter(
            x=filtered_df['month'], 
            y=filtered_df['cumsum_gas_production'], 
            mode='lines', 
            name='Факт товарный с начала года', 
            yaxis='y2',
            fill='tozeroy', 
            line=dict(color="#8bedff")
            )
        )

    fig.add_trace(go.Bar(
        x=filtered_df['month'],
        y=filtered_df['gas_production_value_m3'],  # Столбец с планом добычи
        name='Факт на устье',
        marker_color='#5ca9e0', yaxis='y1'
    ))
    fig.add_trace(go.Bar(
        x=filtered_df['month'],
        y=filtered_df['gas_commercial_value_m3'],  # Столбец с фактом добычи
        name='Факт товарный',
        marker_color='#4a6eb5', yaxis='y1'
    ))
    fig.add_trace(go.Bar(
        x=filtered_df['month'],
        y=filtered_df['gas_commercial_plan_daily_m3'],  # Столбец с фактом добычи
        name='План товарный',
        marker_color='#cf554c', yaxis='y1'
    ))
    fig.add_trace(go.Bar(
        x=filtered_df['month'],
        y=filtered_df['gas_commercial_plan_nomintaion_m3'],  # Столбец с фактом добычи
        name='План номинация',
        marker_color='#6f32a8', yaxis='y1'
    ))
        

    
    fig.add_trace(
        go.Scatter(
            x=filtered_df['month'], 
            y=filtered_df['cumsum_gas_production'], 
            mode='lines', 
            name='Факт на устье с начала года', 
            yaxis='y2', 
            line=dict(color=" royalblue")
            )
        )
    fig.add_trace(
        go.Scatter(
            x=filtered_df['month'], 
            y=filtered_df['cumsum_gas_commercial_plan'], 
            mode='lines', 
            name='План товарный с начала года', 
            yaxis='y2', 
            line=dict(color=" red")
            )
        )
    
    fig.add_trace(
        go.Scatter(
            x=filtered_df['month'], 
            y=filtered_df['cumsum_gas_commercial_nomination'], 
            mode='lines', 
            name='План номинация с начала года', 
            yaxis='y2', 
            line=dict(color="#6f32a8")
            )
        )


    fig.update_layout(
        barmode='group',  # Отображение гистограмм рядом
        xaxis_title='',
        yaxis_title='',
        title='Накопленная добыча и поставка газа за ...',
        yaxis=dict(title='', side='left' ),
        yaxis2=dict(title='', overlaying='y', side='right' ), 
        # legend_title='Legend'
        legend=dict(title='', orientation='h', x=0.5, y=-0.2, xanchor='center', yanchor='top', bgcolor='rgba(255, 255, 255, 0)'),
        xaxis=dict(
            tickmode='array',
            tickvals=list(range(1, 13)),
            ticktext=month_vals
        ),
        hovermode="x unified"
    )

    return fig




# import plotly.express as px
from dash import dcc, html

fig_with_wells = html.Div([
                dcc.Graph(id='first_chart', figure=create_fig_with_wells(year=2023, month=3))
            ])

fig_plus = html.Div([
                dcc.Graph(id='second_chart', figure=create_fig_plus(year=2023))
            ])
