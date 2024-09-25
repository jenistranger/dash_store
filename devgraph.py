import pandas as pd
import plotly.graph_objects as go

# Данные
plan = 1917
fact = 2203
differences = [37, -19, 25, 6]  # Пример промежуточных разниц

# Подготовка данных для построения
labels = ['Plan'] + [f'Step {i+1}' for i in range(len(differences))] + ['Fact']
values = [plan] + differences + [fact]
step_changes = [plan] + [sum(differences[:i]) for i in range(1, len(differences) + 1)]

# Начальные значения для водопада
base_values = [0] + [plan] * len(differences) + [0]

# Диаграмма
fig = go.Figure()

# Добавляем план
fig.add_trace(go.Bar(
    x=[labels[0]],
    y=[values[0]],
    base=[0],
    name='Plan',
    marker=dict(color='blue')
))

# Добавляем промежуточные шаги
for i in range(1, len(differences) + 1):
    color = 'green' if differences[i-1] > 0 else 'red'
    fig.add_trace(go.Bar(
        x=[labels[i]],
        y=[abs(differences[i-1])],
        base=[step_changes[i-1]],
        name=f'Step {i}',
        marker=dict(color=color)
    ))

# Добавляем факт
fig.add_trace(go.Bar(
    x=[labels[-1]],
    y=[fact - plan],
    base=[plan],
    name='Fact',
    marker=dict(color='blue')
))

# Настройки осей и оформление
fig.update_layout(
    title='Waterfall Chart: Plan vs Fact',
    xaxis_title='Steps',
    yaxis_title='Values',
    barmode='stack',
    showlegend=True
)

fig.show()
