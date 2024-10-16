import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px



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


gas_validation = ['project', 'date', 'gas_production_value_m3', 'gas_commercial_value_m3', 'gas_commercial_plan_daily_m3', 'gas_commercial_plan_nomintaion_m3']
condensat_validation = ['project', 'date', 'condensat_production_value_m3', 'condensat_production_weight_t', 'condensat_commercial_value_m3', 'condensat_commercial_weight_t']

def create_fig_with_wells(month, year, title):
    df = pd.read_csv('temp_files\\all_data_from_table.csv')

    df.loc[:, 'date'] = pd.to_datetime(df['date'])
    
    year_to_check = year
    month_to_check = month
    
    filtered_df = df[['project', 'date', 'gas_production_value_m3', 'gas_commercial_value_m3', 'gas_commercial_plan_daily_m3', 'gas_commercial_plan_nomintaion_m3']]
    
    filtered_df = filtered_df[(filtered_df['date'].dt.year == year_to_check) & (filtered_df['date'].dt.month == month_to_check)]

    filtered_df.loc[:, 'day'] = filtered_df['date'].dt.day

    filtered_df['found_total'] = np.random.randint(15, 20, size=len(filtered_df))
    filtered_df['found_active'] = [np.random.randint(10, total) for total in filtered_df['found_total']]
    filtered_df['found_daily_work'] = [np.random.randint(8, active) for active in filtered_df['found_active']]

    filtered_df['deviation'] = (filtered_df['gas_commercial_value_m3']*100/filtered_df['gas_commercial_plan_daily_m3']) - 100
    
    mean_deviation = filtered_df['deviation'].mean()

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=filtered_df['day'], y=(filtered_df['gas_production_value_m3']/1000000), mode='lines', name='Факт на устье', yaxis='y2', line=dict(color="darkblue")))
    fig.add_trace(go.Scatter(x=filtered_df['day'], y=filtered_df['gas_commercial_value_m3']/1000000, mode='lines', name='Факт товарный', yaxis='y2', line=dict(color="royalblue")))
    fig.add_trace(go.Scatter(x=filtered_df['day'], y=filtered_df['gas_commercial_plan_daily_m3']/1000000, mode='lines', name='План суточный', yaxis='y2', line=dict(color="red", dash="dot", width=4)))
    fig.add_trace(go.Scatter(x=filtered_df['day'], y=filtered_df['gas_commercial_plan_nomintaion_m3']/1000000, mode='lines', name='План номинация', yaxis='y2', line=dict(color="#6f32a8")))
    fig.add_trace(go.Bar(x=filtered_df['day'], y=filtered_df['found_total'], name='Фонд скважин', opacity=0.7, yaxis='y1', marker_color='#40a7ff'))
    fig.add_trace(go.Bar(x=filtered_df['day'], y=filtered_df['found_daily_work'], name='В добыче', opacity=0.5, yaxis='y1', marker_color='#797979'))

    # Добавление аннотации с средним отклонением
    fig.add_annotation(
        text=f"Отклонение: {mean_deviation:.2f}%",
        xref="paper", yref="paper",
        x=0.5, y=1.15, showarrow=False,
        font=dict(size=14),
        align="center"
    )

    # Формирование меток оси X
    days_in_month = filtered_df['day'].tolist()  # Получаем все дни месяца
    tickvals = days_in_month
    ticktext = [f'{day:02}.{month:02}' for day in days_in_month]  # Форматирование как дд.мм


    fig.update_layout(
        title=f'Суточная добыча и поставка газа (unit) за {month}.{year}, <span style="color:red;">{title}</span>',
        xaxis_title='',
        yaxis_title='Объем',
        yaxis2=dict(
            title='млн.м<sup>3</sup>', 
            overlaying='y', 
            side='left'
        ), 
        yaxis=dict(title='Скважины', side='right'),
        barmode='overlay', 
        legend=dict(title='', orientation='h', x=0.5, y=-0.2, xanchor='center', yanchor='top', bgcolor='rgba(255, 255, 255, 0)'),
        hovermode="x unified",
        xaxis=dict(
            tickvals=tickvals,
            ticktext=ticktext,
            tickmode='array',
            tickangle=45
        )
    )

    return fig








def create_fig_with_wells_periods(start_date, end_date, period):
    df = pd.read_csv('temp_files\\all_data_from_table.csv')

    df.loc[:, 'date'] = pd.to_datetime(df['date'])
    
    if period == 'month':
        pass




    elif period == 'period':
        pass


























def create_fig_plus(year, title):
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

    df.loc[:, 'date'] = pd.to_datetime(df['date'])
    df.loc[:, 'month'] = df['date'].dt.month
    df.loc[:, 'year'] = df['date'].dt.year

    grouped_df = df.groupby(['year', 'month']).sum(numeric_only=True).reset_index()
    
    year_to_filter = year

    filtered_df = grouped_df[grouped_df['year'] == year_to_filter]

    filtered_df.loc[:, 'cumsum_gas_production'] = filtered_df['gas_production_value_m3'].cumsum()    
    filtered_df.loc[:, 'cumsum_gas_commercial'] = filtered_df['gas_commercial_value_m3'].cumsum()    
    filtered_df.loc[:, 'cumsum_gas_commercial_plan'] = filtered_df['gas_commercial_plan_daily_m3'].cumsum()
    filtered_df.loc[:, 'cumsum_gas_commercial_nomination'] = filtered_df['gas_commercial_plan_nomintaion_m3'].cumsum()

    filtered_df['deviation'] = (filtered_df['cumsum_gas_commercial']*100/filtered_df['cumsum_gas_commercial_plan']) - 100
    mean_deviation = filtered_df['deviation'].mean()

    fig = go.Figure()
    

    fig.add_annotation(
        text=f"Отклонение: {mean_deviation:.2f}%",
        xref="paper", yref="paper",
        x=0.5, y=1.15, showarrow=False,
        font=dict(size=14),
        align="center"
    )

    fig.add_trace(
        go.Scatter(
            x=filtered_df['month'], 
            y=filtered_df['cumsum_gas_commercial'], 
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
        title=f'Накопленная добыча и поставка газа (unit) за {year}, <span style="color:red;">{title}</span>',
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


def waterfall_graph():
    # Тестовые данные
    projects = ['A', 'B', 'C', 'D', 'E', 'F']
    plan = [1917, 1800, 1750, 1600, 1500, 1700]
    fact = [2047, 1819, 1747, 1651, 1600, 1724]


    # Сортировка данных по плану
    sorted_data = sorted(zip(plan, fact, projects), key=lambda x: x[0])
    plan_sorted, fact_sorted, projects_sorted = zip(*sorted_data)

    # Вычисляем разницу между фактом и планом
    diff = [f - p for f, p in zip(fact_sorted, plan_sorted)]
    colors = ['#0ea64d' if d > 0 else '#e24931' for d in diff]
    annotations = [f'+{d}' if d > 0 else f'{d}' for d in diff]

    # Создание графика
    fig = go.Figure()

    fig.add_annotation(
        text=f"Выполнение плана по (fluid) за (period), (unit)",
        xref="paper", yref="paper",
        x=0.5, y=1.15, showarrow=False,
        font=dict(size=14),
        align="center"
    )


    for i, project in enumerate(projects_sorted):
        fig.add_trace(go.Bar(
            x=[project],
            y=[fact_sorted[i] - plan_sorted[i]],  # Разница между фактом и планом
            name=f'{project}: {fact_sorted[i] - plan_sorted[i]}',
            marker_color=colors[i],
            base=plan_sorted[i],  # Уровень плана - начало гистограммы
            width=0.5,
        ))

    # Добавление аннотаций с разницей
    for i, project in enumerate(projects_sorted):
        fig.add_annotation(
            x=project,

            y=fact_sorted[i],  # Фактический уровень

            text=annotations[i],
            showarrow=False,
            yshift=10
        )

    # Настройки графика
    fig.update_layout(
        yaxis=dict(
            range=[0, int(max(fact_sorted)+max(fact_sorted)/100*20)],
        ),
        title="Динамика отклонений от плана объёма за ...",
        yaxis_title="",
        xaxis_title="Проекты",
        legend=dict(title='', orientation='h', x=0.5, y=-0.2, xanchor='center', yanchor='top', bgcolor='rgba(255, 255, 255, 0)'),
        showlegend=False
    )

    # Отображение графика
    return fig



import pandas as pd



# import plotly.express as px
from dash import dcc, html

fig_with_wells = html.Div([
                dcc.Graph(id='first_chart', figure=create_fig_with_wells(year=2024, month=5, title="Загрузка..."))
            ])

fig_plus = html.Div([
                dcc.Graph(id='second_chart', figure=create_fig_plus(year=2024, title="Загрузка..."))
            ])

fig_waterfall = html.Div([
                dcc.Graph(id='third_chart', figure=waterfall_graph())
            ])



from datetime import datetime, date

#0 - месяц, 1 - год, 2 - весь датафрейм
def get_actual_data():
    df = pd.read_csv('temp_files\\all_data_from_table.csv')
    df["date"] = pd.to_datetime(df['date'])
    max_date = df['date'].max()
    actual_year = max_date.year
    actual_month = max_date.month
    actual_df = df[(df['date'].dt.year == actual_year) & (df['date'].dt.month == actual_month)]
    return actual_month, actual_year, actual_df



def get_gas_stats_monthly(month, year):

    df = pd.read_csv('temp_files\\all_data_from_table.csv')
    df['date'] = pd.to_datetime(df['date'])
    
    filtered_df = df[['project', 'date', 'gas_commercial_value_m3']]
    

    target_year = year 
    target_month = month 

    if target_month > 1:
        current_month_data = filtered_df[(filtered_df['date'].dt.year == target_year) & (filtered_df['date'].dt.month == target_month)]
        previous_month_data = filtered_df[(filtered_df['date'].dt.year == target_year) & (filtered_df['date'].dt.month == target_month - 1)]
        current_year_data = filtered_df[filtered_df['date'].dt.year == target_year]
        previous_year_data = filtered_df[filtered_df['date'].dt.year == target_year - 1]
    
    else:
    
        current_month_data = filtered_df[(filtered_df['date'].dt.year == target_year) & (filtered_df['date'].dt.month == target_month)]
        previous_month_data = filtered_df[(filtered_df['date'].dt.year == target_year-1) & (filtered_df['date'].dt.month == 12)]
        current_year_data = filtered_df[filtered_df['date'].dt.year == target_year]
        previous_year_data = filtered_df[filtered_df['date'].dt.year == target_year - 1]

    
    current_month_sum = current_month_data['gas_commercial_value_m3'].sum() if not current_month_data.empty else 0
    previous_month_sum = previous_month_data['gas_commercial_value_m3'].sum() if not previous_month_data.empty else 0
    difference_by_month = current_month_sum - previous_month_sum
    percentage_by_month =   (current_month_sum*100/previous_month_sum)-100 if previous_month_sum != 0 else 0 
    
    current_year_sum = current_year_data['gas_commercial_value_m3'].sum() if not current_year_data.empty else 0
    previous_year_sum = previous_year_data['gas_commercial_value_m3'].sum() if not previous_year_data.empty else 0
    difference_by_year = current_year_sum - previous_year_sum
    percentage_by_year =   (current_year_sum*100/previous_year_sum)-100 if previous_year_sum != 0 else 0 

    result = {
        "current_month_sum" : current_month_sum,
        "previous_month_sum" : previous_month_sum,
        "difference_by_month" : difference_by_month,
        "percentage_by_month" : percentage_by_month,
        "current_year_sum" : current_year_sum,
        "previous_year_sum" : previous_year_sum,
        "difference_by_year" : difference_by_year,
        "percentage_by_year" : percentage_by_year,

    }
    
    return result


def from_period(start, end):
    df = pd.read_csv('temp_files\\all_data_from_table.csv')
    df['date'] = pd.to_datetime(df['date'])
    start = pd.to_datetime(start)
    end = pd.to_datetime(end)
    period_df = df.loc[df['date'].between(start, end, inclusive=True)]
    print(period_df)

