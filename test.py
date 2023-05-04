import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import plotly
import plotly.express as px
import matplotlib.colors

# Тэги колонок 
names_col = ["Bandwidth","Simulated channel delay","Simulated jitter","Error percentage",
             "Packet size in bytes","Planned transmission rate","IP","Number of packets sent",
             "number of packets received", "Size of sent data","size of received data in bytes",
             "Time in seconds spent on the test","Actual bandwidth used","Minimum Delay Size",
             "Maximum Delay Size","Average delay time","Test number within the experiment"]

# читаем  DF
result = pd.read_csv('logs/bwtest3.log', delimiter=',',names=names_col)
#df2 = pd.read_csv('logs/bwtest2.log', delimiter=',',names=names_col)

##result = pd.concat(results)


#Группируем DF в группы по фиксированным значеням 
#result = result.groupby(["Bandwidth","Simulated channel delay","Simulated jitter","Error percentage",
             #"Packet size in bytes","Planned transmission rate","IP","Number of packets sent","Size of sent data"]).mean()



#(result["Minimum Delay Size"].corr(result["Maximum Delay Size"]))
# corr Max Aver 0.014953319302063192
# corr Min Aver 0.08625733023146863
# corr Min Max -0.11998446042316785

# for index, frame in enumerate(result2):
#     print(f"{index} Среднее:")
#     print(frame[1].mean())    
x=result["Average delay time"].tolist()
cm = plt.get_cmap("YlOrRd")
norm = matplotlib.colors.Normalize(vmin=0, vmax=1)
fig =  go.Figure(
                data=[
                        go.Scatter3d(
                                    x = x, 
                                    y = result["Minimum Delay Size"].tolist(), 
                                    z = result["Maximum Delay Size"].tolist(),
                                    mode='markers',
                                    name = "AMM",
                                    text=[f"Номер {i}" for i in range(1,len(result)+1)],
                                    marker = dict(
                                    size = 12,
                                    color = cm(norm([float(i)/(len(result)+1) for i in range(1,len(result)+1)])), # set color to an array/list of desired values
                                    #colorscale = 'Viridis'
                                                )
                                    ) 
                    ],
                layout=go.Layout(
                                showlegend=True,
                                legend_orientation="h",
                                legend=dict(x=.5, xanchor="center"),
                                title= f"""Визуализация эксперементов AVG по всем параметрам """,
                                scene=dict(
                                        xaxis=dict( title="Average Delay time"),
                                        yaxis=dict( title="Minimum Delay Size"),
                                        zaxis=dict(title="Maximum Delay Size"),
                                            )
                                ),
                                
                )       


plotly.offline.plot( fig,
                    auto_open=True,
                    filename=(f"./graphs/3DPlotAVGALL.html"))
                    