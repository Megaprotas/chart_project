from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

plt.style.use('seaborn')

TITLE = 'Some Scatter Chart'
XLABEL = 'Age'
YLABEL = 'Quantity'
OPACITY = 0.3

data = pd.read_csv('data3.csv')
xaxis = data['xaxis']
yankees = data['yankees']
color = data['color']
sizes = data['sizes']

plt.scatter(xaxis, yankees, s=sizes, c=color, cmap='Blues', edgecolor='black', linewidths=1, alpha=0.5)

# plt.xscale('log')
# plt.yscale('log')

plt.title(TITLE)
plt.xlabel(XLABEL)
plt.ylabel(YLABEL)
plt.xticks(xaxis)
plt.grid(True, which='both', alpha=OPACITY)

cbar = plt.colorbar()
cbar.set_label('Stats')

plt.tight_layout()
plt.show()