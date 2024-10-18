from dash import html, dcc, Output, Input, callback, State, callback_context
from devparser import get_actual_data, create_fig_plus, get_gas_stats_monthly, from_period, figure_with_wells_gas, figure_with_wells_condensat, test_with_wells, common_figure_wells
from datetime import date
from datetime import datetime

#показать/скрыть дейтпикер
@callback(
    Output('date-picker-range', 'style'),
    Input('period-radioitems', 'value')
)
def toggle_date_picker(selected_value):
    if selected_value == 'period':
        return {'display': 'block'}  # Показываем дейтпикер
    return {'display': 'none'} 

#тестовый вывод даты
@callback(
    Output("output-date-picker", "children"),
    Input("date-picker-range", "start_date"),
    Input("date-picker-range", "end_date")
)
def update_output(start_date, end_date):
    if start_date and end_date:
        return f"Выбранный период: с {start_date} по {end_date} || {type(start_date)}"
    return None



#отрисовка графиков и статы при выборе периода

@callback(
    [
        Output("first_chart", "figure"),
        Output("second_chart", "figure"),
        Output("output-month-picker", "children"),
        Output("total_gas_value", "children"),  # для обновления общего значения газа
        Output("month_change", "children"),  # для обновления изменения за месяц
        Output("month_change", "style"),     # для изменения цвета текста
        Output("year_change", "children"),   # для обновления изменения за год
        Output("year_change", "style")       # для изменения цвета текста
    ],
    [Input("period-radioitems", "value"),
    Input("date-picker-range", "start_date"),
    Input("date-picker-range", "end_date"),
    Input('hydrocarbons-checklist', "value")]
)
def update_output(value, start_date, end_date, fluid):
    if value == 'month':
        props = get_actual_data()
        stats = get_gas_stats_monthly(props[0], props[1])

        fig1 = common_figure_wells(period='month', fluids=fluid, month=props[0], year=props[1])
        fig2 = create_fig_plus(props[1], "(актуальный месяц)")
        month_change_text = f"Месяц: {(stats['difference_by_month']/1000000):.2f} | {stats['percentage_by_month']:.2f}%"
        month_change_style = {"color": "#0ea64d"} if stats['percentage_by_month'] >= 0 else {"color": "#e24931"}

        # Формируем текст и стиль для изменения за год
        year_change_text = f"Год: {(stats['difference_by_year']/1000000):.2f} | {stats['percentage_by_year']:.2f}%"
        year_change_style = {"color": "#0ea64d"} if stats['percentage_by_year'] >= 0 else {"color": "#e24931"}

        total_gas_value = f"{(stats['current_month_sum']/1000000):.1f}"
        return (
            fig1, 
            fig2, 
            f"Актуальный месяц сейчас - {datetime.now().month-1}\nПо данным - {props[0]}", 
            total_gas_value,
            month_change_text,
            month_change_style,
            year_change_text,
            year_change_style
        )
       
    elif value == 'period':
        props = get_actual_data()
        stats = get_gas_stats_monthly(props[0], props[1])
        if start_date and end_date:
            start = datetime.strptime(start_date, "%Y-%m-%d").date()
            end = datetime.strptime(end_date, "%Y-%m-%d").date()
            fig1 = common_figure_wells(period='period', fluids=fluid, start_date=start, end_date=end)
        else:
            fig1 = common_figure_wells(period='month', fluids=fluid, month=props[0], year=props[1])

            
        # Создаем графики
        # fig1 = create_fig_with_wells(props[0], props[1], "(актуальный месяц)")
        fig2 = create_fig_plus(props[1], "(актуальный месяц)")

        # Формируем текст и стиль для изменения за месяц
        month_change_text = f"Месяц: {(stats['difference_by_month']/1000000):.2f} | {stats['percentage_by_month']:.2f}%"
        month_change_style = {"color": "#0ea64d"} if stats['percentage_by_month'] >= 0 else {"color": "#e24931"}

        # Формируем текст и стиль для изменения за год
        year_change_text = f"Год: {(stats['difference_by_year']/1000000):.2f} | {stats['percentage_by_year']:.2f}%"
        year_change_style = {"color": "#0ea64d"} if stats['percentage_by_year'] >= 0 else {"color": "#e24931"}

        # Обновляем общую сумму газа
        total_gas_value = f"{(stats['current_month_sum']/1000000):.1f}"
        return (
            fig1, 
            fig2, 
            f"Актуальный месяц сейчас - {datetime.now().month-1}\nПо данным - {props[0]}", 
            total_gas_value,
            month_change_text,
            month_change_style,
            year_change_text,
            year_change_style
        )
    return {}, {}, None, "", "", {}, "", {}

        # if "газ" in fluid:
        #     props = get_actual_data()
        #     stats = get_gas_stats_monthly(props[0], props[1])
        #     if start_date and end_date:
        #         start = datetime.strptime(start_date, "%Y-%m-%d").date()
        #         end = datetime.strptime(end_date, "%Y-%m-%d").date()
        #         fig1 = figure_with_wells_gas(period='period', start_date=start, end_date=end)
        #     else:
        #         fig1 = figure_with_wells_gas(period='month', month=props[0], year=props[1])

                
        #     # Создаем графики
        #     # fig1 = create_fig_with_wells(props[0], props[1], "(актуальный месяц)")
        #     fig2 = create_fig_plus(props[1], "(актуальный месяц)")

        #     # Формируем текст и стиль для изменения за месяц
        #     month_change_text = f"Месяц: {(stats['difference_by_month']/1000000):.2f} | {stats['percentage_by_month']:.2f}%"
        #     month_change_style = {"color": "#0ea64d"} if stats['percentage_by_month'] >= 0 else {"color": "#e24931"}

        #     # Формируем текст и стиль для изменения за год
        #     year_change_text = f"Год: {(stats['difference_by_year']/1000000):.2f} | {stats['percentage_by_year']:.2f}%"
        #     year_change_style = {"color": "#0ea64d"} if stats['percentage_by_year'] >= 0 else {"color": "#e24931"}

        #     # Обновляем общую сумму газа
        #     total_gas_value = f"{(stats['current_month_sum']/1000000):.1f}"
        #     return (
        #         fig1, 
        #         fig2, 
        #         f"Актуальный месяц сейчас - {datetime.now().month-1}\nПо данным - {props[0]}", 
        #         total_gas_value,
        #         month_change_text,
        #         month_change_style,
        #         year_change_text,
        #         year_change_style
        #     )
        # elif "конденсат" in fluid:
        #     props = get_actual_data()
        #     stats = get_gas_stats_monthly(props[0], props[1])
        #     if start_date and end_date:
        #         start = datetime.strptime(start_date, "%Y-%m-%d").date()
        #         end = datetime.strptime(end_date, "%Y-%m-%d").date()
        #         fig1 = figure_with_wells_condensat(period='period', start_date=start, end_date=end)
        #     else:
        #         fig1 = figure_with_wells_condensat(period='month', month=props[0], year=props[1])

        #     # Создаем графики
        #     # fig1 = create_fig_with_wells(props[0], props[1], "(актуальный месяц)")
        #     fig2 = create_fig_plus(props[1], "(актуальный месяц)")

        #     # Формируем текст и стиль для изменения за месяц
        #     month_change_text = f"Месяц: {(stats['difference_by_month']/1000000):.2f} | {stats['percentage_by_month']:.2f}%"
        #     month_change_style = {"color": "#0ea64d"} if stats['percentage_by_month'] >= 0 else {"color": "#e24931"}

        #     # Формируем текст и стиль для изменения за год
        #     year_change_text = f"Год: {(stats['difference_by_year']/1000000):.2f} | {stats['percentage_by_year']:.2f}%"
        #     year_change_style = {"color": "#0ea64d"} if stats['percentage_by_year'] >= 0 else {"color": "#e24931"}

        #     # Обновляем общую сумму газа
        #     total_gas_value = f"{(stats['current_month_sum']/1000000):.1f}"
        #     return (
        #         fig1, 
        #         fig2, 
        #         f"Актуальный месяц сейчас - {datetime.now().month-1}\nПо данным - {props[0]}", 
        #         total_gas_value,
        #         month_change_text,
        #         month_change_style,
        #         year_change_text,
        #         year_change_style
        #     )
        
    # Если не выбран месяц, возвращаем пустые данные
    # return {}, {}, None, "", "", {}, "", {}


#чекбокс с all
options_assets = ['Ипати Акио', 'Блоки 05-2/05-3', 'Шахпахты', 'ВИНЗ']
@callback(
    Output("projects-checklist", "value"),
    Output("all-checklist", "value"),
    Input("projects-checklist", "value"),
    Input("all-checklist", "value"),
)
def sync_checklists(projects_checklist, all_selected):
    ctx = callback_context
    input_id = ctx.triggered[0]["prop_id"].split(".")[0]

    if input_id == "projects-checklist":
        if set(projects_checklist) == set(options_assets):
            all_selected = ["Все"]
        else:
            all_selected = []
    else:
        projects_checklist = options_assets if all_selected else []

    return projects_checklist, all_selected





#работа с колапсами

@callback(
    Output("collapse-units", "is_open"),
    [Input("collapse-button-units", "n_clicks")],
    [State("collapse-units", "is_open")],
)
def toggle_collapse_units(n, is_open):
    if n:
        return not is_open
    return is_open

@callback(
    Output("collapse-period", "is_open"),
    [Input("collapse-button-period", "n_clicks")],
    [State("collapse-period", "is_open")],
)
def toggle_collapse_periods(n, is_open):
    if n:
        return not is_open
    return is_open

@callback(
    Output("collapse-hydrocarbons", "is_open"),
    [Input("collapse-button-hydrocarbons", "n_clicks")],
    [State("collapse-hydrocarbons", "is_open")],
)
def toggle_collapse_hydrocarbons(n, is_open):
    if n:
        return not is_open
    return is_open


@callback(
    Output("collapse-projects", "is_open"),
    [Input("collapse-button-projects", "n_clicks")],
    [State("collapse-projects", "is_open")],
)
def toggle_collapse_projects(n, is_open):
    if n:
        return not is_open
    return is_open




#тестовый вывод

@callback(
    Output("radioitems-checklist-output", "children"),
    [Input("period-radioitems", "value"),
     Input("hydrocarbons-checklist", "value"),
     Input("projects-checklist", "value"),
     Input("units-radioitems", "value"),
     ]
)
def on_form_change(radio_items_value, hc_velues, projects, units):
    template = f"Период: {radio_items_value}, УВ: {hc_velues}, Проект: - {projects}, ЕИ: {units} selected."
    return template
