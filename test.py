import matplotlib.pyplot as plt
import random

fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(projection='3d')

sequence_containing_x_vals = list(range(0, 100))
sequence_containing_y_vals = list(range(0, 100))
sequence_containing_z_vals = list(range(0, 100))

import plotly.express as px

fig = px.scatter_3d(x=sequence_containing_x_vals,y=sequence_containing_y_vals, z=sequence_containing_x_vals)
fig.show()
fig =  go.Figure(data=[
            go.Scatter3d(df = grouped.data,
                        x = grouped2[0][1]["Average delay time"].tolist(), 
                        y = grouped2[0][1]["Minimum Delay Size"].tolist(), 
                        z = grouped2[0][1]["Maximum Delay Size"].tolist(),
                        mode='markers'
                        ) 
                     ])