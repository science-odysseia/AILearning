import plotly.graph_objects as go
import numpy as np

x = np.linspace(0, 10, 20) # 일부러 점을 적게 줌 (20개)
y = np.sin(x)

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=x, y=y,
    mode='lines+markers',
    line=dict(shape='spline', smoothing=1.3), # 점이 적어도 곡선으로 그려줌
    name='Sine Spline'
))
fig.show() # 노트북 셀 안에 바로 뜹니다.