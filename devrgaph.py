def create_fig_with_wells_period(start_date, end_date, title):
    df = pd.read_csv('temp_files\\all_data_from_table.csv')
    df.loc[:, 'date'] = pd.to_datetime(df['date'])

    # Преобразуем start_date и end_date в формат datetime
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

    # Фильтруем данные по диапазону дат
    filtered_df = df[['project', 'date', 'gas_production_value_m3', 'gas_commercial_value_m3', 
                      'gas_commercial_plan_daily_m3', 'gas_commercial_plan_nomintaion_m3']]
    filtered_df = filtered_df[(filtered_df['date'] >= start_date) & (filtered_df['date'] <= end_date)]
    
    total_days = len(filtered_df['date'].unique())
    
    if total_days < 35:
        # Считаем по дням
        filtered_df.loc[:, 'day'] = filtered_df['date'].dt.day
        filtered_df['found_total'] = np.random.randint(15, 20, size=len(filtered_df))
        filtered_df['found_active'] = [np.random.randint(10, total) for total in filtered_df['found_total']]
        filtered_df['found_daily_work'] = [np.random.randint(8, active) for active in filtered_df['found_active']]
        filtered_df['deviation'] = (filtered_df['gas_commercial_value_m3'] * 100 / filtered_df['gas_commercial_plan_daily_m3']) - 100

        mean_deviation = filtered_df['deviation'].mean()

        fig = go.Figure()

        # Добавляем линии и бары на график
        fig.add_trace(go.Scatter(x=filtered_df['date'], y=(filtered_df['gas_production_value_m3'] / 1000000), 
                                 mode='lines', name='Факт на устье', yaxis='y2', line=dict(color="darkblue")))
        fig.add_trace(go.Scatter(x=filtered_df['date'], y=filtered_df['gas_commercial_value_m3'] / 1000000, 
                                 mode='lines', name='Факт товарный', yaxis='y2', line=dict(color="royalblue")))
        fig.add_trace(go.Scatter(x=filtered_df['date'], y=filtered_df['gas_commercial_plan_daily_m3'] / 1000000, 
                                 mode='lines', name='План суточный', yaxis='y2', line=dict(color="red", dash="dot", width=4)))
        fig.add_trace(go.Scatter(x=filtered_df['date'], y=filtered_df['gas_commercial_plan_nomintaion_m3'] / 1000000, 
                                 mode='lines', name='План номинация', yaxis='y2', line=dict(color="#6f32a8")))
        fig.add_trace(go.Bar(x=filtered_df['date'], y=filtered_df['found_total'], name='Фонд скважин', 
                             opacity=0.7, yaxis='y1', marker_color='#40a7ff'))
        fig.add_trace(go.Bar(x=filtered_df['date'], y=filtered_df['found_daily_work'], name='В добыче', 
                             opacity=0.5, yaxis='y1', marker_color='#797979'))

        # Формирование меток оси X по дням
        days_in_period = filtered_df['date'].tolist()
        tickvals = days_in_period
        ticktext = [date.strftime('%d.%m') for date in days_in_period]

    elif total_days <= 365:
        # Считаем по месяцам
        filtered_df['month'] = filtered_df['date'].dt.to_period('M')  # Агрегируем по месяцам
        filtered_df = filtered_df.groupby('month').sum().reset_index()
        
        mean_deviation = (filtered_df['gas_commercial_value_m3'] * 100 / filtered_df['gas_commercial_plan_daily_m3'] - 100).mean()

        fig = go.Figure()

        # Добавляем линии и бары на график
        fig.add_trace(go.Scatter(x=filtered_df['month'].astype(str), y=(filtered_df['gas_production_value_m3'] / 1000000), 
                                 mode='lines', name='Факт на устье', yaxis='y2', line=dict(color="darkblue")))
        fig.add_trace(go.Scatter(x=filtered_df['month'].astype(str), y=filtered_df['gas_commercial_value_m3'] / 1000000, 
                                 mode='lines', name='Факт товарный', yaxis='y2', line=dict(color="royalblue")))
        fig.add_trace(go.Scatter(x=filtered_df['month'].astype(str), y=filtered_df['gas_commercial_plan_daily_m3'] / 1000000, 
                                 mode='lines', name='План суточный', yaxis='y2', line=dict(color="red", dash="dot", width=4)))
        fig.add_trace(go.Scatter(x=filtered_df['month'].astype(str), y=filtered_df['gas_commercial_plan_nomintaion_m3'] / 1000000, 
                                 mode='lines', name='План номинация', yaxis='y2', line=dict(color="#6f32a8")))

        # Формирование меток оси X по месяцам
        tickvals = filtered_df['month'].astype(str).tolist()
        ticktext = [f'{month.strftime("%m.%Y")}' for month in filtered_df['month']]

    else:
        # Считаем по годам
        filtered_df['year'] = filtered_df['date'].dt.year  # Агрегируем по годам
        filtered_df = filtered_df.groupby('year').sum().reset_index()

        mean_deviation = (filtered_df['gas_commercial_value_m3'] * 100 / filtered_df['gas_commercial_plan_daily_m3'] - 100).mean()

        fig = go.Figure()

        # Добавляем линии и бары на график
        fig.add_trace(go.Scatter(x=filtered_df['year'], y=(filtered_df['gas_production_value_m3'] / 1000000), 
                                 mode='lines', name='Факт на устье', yaxis='y2', line=dict(color="darkblue")))
        fig.add_trace(go.Scatter(x=filtered_df['year'], y=filtered_df['gas_commercial_value_m3'] / 1000000, 
                                 mode='lines', name='Факт товарный', yaxis='y2', line=dict(color="royalblue")))
        fig.add_trace(go.Scatter(x=filtered_df['year'], y=filtered_df['gas_commercial_plan_daily_m3'] / 1000000, 
                                 mode='lines', name='План суточный', yaxis='y2', line=dict(color="red", dash="dot", width=4)))
        fig.add_trace(go.Scatter(x=filtered_df['year'], y=filtered_df['gas_commercial_plan_nomintaion_m3'] / 1000000, 
                                 mode='lines', name='План номинация', yaxis='y2', line=dict(color="#6f32a8")))

        # Формирование меток оси X по годам
        tickvals = filtered_df['year'].tolist()
        ticktext = [str(year) for year in tickvals]

    # Добавляем аннотацию с средним отклонением
    fig.add_annotation(
        text=f"Отклонение: {mean_deviation:.2f}%",
        xref="paper", yref="paper",
        x=0.5, y=1.15, showarrow=False,
        font=dict(size=14),
        align="center"
    )

    # Обновляем макет графика
    fig.update_layout(
        title=f'Суточная добыча и поставка газа (unit) за период {start_date.strftime("%d.%m.%Y")} - {end_date.strftime("%d.%m.%Y")}, <span style="color:red;">{title}</span>',
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
            tickangle=45
        )
    )

    return fig
