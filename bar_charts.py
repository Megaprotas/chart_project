from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

TITLE = 'Bar chart'
XLABEL = 'Age'
YLABEL = 'Attendance'
BLUE = '#1c2841'
RED = '#C41E3A'
GREEN = '#78AB46'
OPACITY = 0.3
MIN_Y_VAL = 0
MAX_Y_VAL = 400

data = pd.read_csv('data.csv')

xaxis = data['xaxis']
yankees = data['yankees']
cards = data['cards']
dbacks = data['dbacks']

x_index = np.arange(len(xaxis))
width = 0.25

plt.bar(x_index - width, yankees, width=width, color=BLUE, label='Yankees')
plt.bar(x_index, cards, width=width, color=RED, label='Cardinals')
plt.bar(x_index + width, dbacks, width=width, color=GREEN, label='Dbacks')

plt.tight_layout()
plt.title(TITLE)
plt.legend()
plt.grid(True, which='both', alpha=OPACITY)

plt.xlabel(XLABEL)
plt.ylabel(YLABEL)

plt.xticks(ticks=x_index, labels=xaxis)
plt.ylim(MIN_Y_VAL, MAX_Y_VAL)

plt.show()