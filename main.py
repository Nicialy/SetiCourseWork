import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import plotly
import plotly.express as px

# Тэги колонок 
names_col = ["Bandwidth","Simulated channel delay","Simulated jitter","Error percentage",
             "Packet size in bytes","Planned transmission rate","IP","Number of packets sent",
             "number of packets received", "Size of sent data","size of received data in bytes",
             "Time in seconds spent on the test","Actual bandwidth used","Minimum Delay Size",
             "Maximum Delay Size","Average delay time","Test number within the experiment"]

# читаем  DF
df1 = pd.read_csv('Logs/bwtest.log', delimiter=',',names=names_col)
df2 = pd.read_csv('Logs/bwtest2.log', delimiter=',',names=names_col)

frames = [df1, df2]
result = pd.concat(frames)


#Группируем DF в группы по фиксированным значеням 
grouped = result.groupby(["Bandwidth","Simulated channel delay","Simulated jitter","Error percentage",
             "Packet size in bytes","Planned transmission rate","IP","Number of packets sent","Size of sent data"])


# Получаем List group
grouped2 = list(grouped)
print(grouped2)

# рисуем точки

for index, frame in enumerate(grouped2):

    bandwidth = frame[1]["Bandwidth"].head(1).item()
    ch_delay = frame[1]["Simulated channel delay"].head(1).item()
    jitter = frame[1]["Simulated jitter"].head(1).item()
    fig =  go.Figure(
                    data=[
                            go.Scatter3d(
                                        x = frame[1]["Average delay time"].tolist(), 
                                        y = frame[1]["Minimum Delay Size"].tolist(), 
                                        z = frame[1]["Maximum Delay Size"].tolist(),
                                        mode='markers',
                                        name = "AMM"
                                        ) 
                        ],
                    layout=go.Layout(
                                    showlegend=True,
                                    legend_orientation="h",
                                    legend=dict(x=.5, xanchor="center"),
                                    title= f"""Визуализация эксперементов №{index + 1} Bandwidth = {bandwidth} Ch.delay = {ch_delay} Jitter = {jitter} """,
                                    scene=dict(
                                            xaxis=dict( title="Average Delay time"),
                                            yaxis=dict( title="Minimum Delay Size"),
                                            zaxis=dict(title="Maximum Delay Size"),
                                                )
                                    ),
                                    
                    )       


    plotly.offline.plot( fig,
                        auto_open=False,
                        filename=(f"./Graphs/3DPlot№{index + 1}.html"))
                        