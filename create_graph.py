import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import plotly
import matplotlib.colors
import plotly.express as px
from uuid import UUID


# Тэги колонок 
names_col = ["Bandwidth","Simulated channel delay","Simulated jitter","Error percentage",
             "Packet size in bytes","Planned transmission rate","IP","Number of packets sent",
             "number of packets received", "Size of sent data","size of received data in bytes",
             "Time in seconds spent on the test","Actual bandwidth used","Minimum Delay Size",
             "Maximum Delay Size","Average delay time","Test number within the experiment"]

# читаем  DF
#df1 = pd.read_csv('logs/bwtest.log', delimiter=',',names=names_col)
def create_draft(file_name: str, id: UUID):
    result = pd.read_csv(f'app/assets/{file_name}', delimiter=',',names=names_col)

    #groupeds = [df1, df2]
    #result = df2


    #Группируем DF в группы по фиксированным значеням 
    grouped = result.groupby(["Bandwidth","Simulated channel delay","Simulated jitter","Error percentage",
                "Packet size in bytes","Planned transmission rate","IP","Number of packets sent","Size of sent data"]).mean()


    # Получаем List group
    grouped2 = list(grouped)

    # рисуем точки


        #bandwidth = grouped["Bandwidth"].head(1).item()
        #ch_delay = grouped["Simulated channel delay"].head(1).item()
        #jitter = grouped["Simulated jitter"].head(1).item()
    cm = plt.get_cmap("YlOrRd")
    norm = matplotlib.colors.Normalize()
    x = list(set(result["Packet size in bytes"].tolist()))
    x.sort()
    fig =  go.Figure(
                    data=[
                            go.Scatter(
                                        x = x, 
                                        y = grouped["Minimum Delay Size"].tolist(), 
                                        #z = grouped["Maximum Delay Size"].tolist(),
                                        mode='markers',
                                        name = "Minimum",
                                        text=[f"Номер {i}" for i in range(1,len(grouped)+1)],
                                        marker = dict(
                                            size = 12,
                                            color = 'green', # set color to an array/list of desired values
                                            #colorscale = 'Viridis',
                                            opacity = 0.8
                                            ),
                                        ),

                            go.Scatter(
                                        x = x, 
                                        y = grouped["Average delay time"].tolist(), 
                                        #z = grouped["Maximum Delay Size"].tolist(),
                                        mode='markers',
                                        name = "Average",
                                        text=[f"Номер {i}" for i in range(1,len(grouped)+1)],
                                        marker = dict(
                                            size = 12,
                                            color = 'red', # set color to an array/list of desired values
                                            #colorscale = 'Viridis',
                                            opacity = 0.8
                                            ),
                                        ),
                            go.Scatter(
                                        x = x, 
                                        y = grouped["Maximum Delay Size"].tolist(), 
                                        #z = grouped["Maximum Delay Size"].tolist(),
                                        mode='markers',
                                        name = "Maximum",
                                        text=[f"Номер {i}" for i in range(1,len(grouped)+1)],
                                        marker = dict(
                                            size = 12,
                                            color = 'blue', # set color to an array/list of desired values
                                            colorscale = 'Viridis',
                                            opacity = 0.8
                                            ),
                                        ) 
                        ],
                    layout=go.Layout(
                                    showlegend=True,
                                    legend_orientation="h",
                                    legend=dict(x=.5, xanchor="center"),
                                    title= f"""Визуализация эксперементов AVG по всем параметрам """,
                                    scene=dict(
                                            xaxis=dict( title="Packet size in bytes"),
                                            yaxis=dict( title="ms"),
                                            #zaxis=dict(title="Maximum Delay Size"),
                                                )
                                    ),
                    )       
    filepath="./app/assets/"
    filename = f"2DPlotAVGLog3{id}.html"
    plotly.offline.plot( fig,
                        auto_open=False,
                        filename=filepath+filename)
    return filename
                        