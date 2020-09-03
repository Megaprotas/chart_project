from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

# xaxis = [25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
# yankees = [410, 450, 289, 412, 351, 345, 230, 129, 345, 320, 126, 455, 387, 288, 233, 301]
# cards = [380, 444, 289, 389, 410, 285, 345, 128, 375, 333, 275, 345, 401, 347, 115, 156]
TITLE = 'Ticket Sales (Q.ty) by Age Group'
XLABEL = 'Age'
YLABEL = 'Quantity'
BLUE = '#1c2841'
RED = '#C41E3A'
GREEN = '#00FF00'
OPACITY = 0.3

data = pd.read_csv('data.csv')
xaxis = data['xaxis']
yankees = data['yankees']
cards = data['cards']
dbacks= data['dbacks']

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True, sharey=True)

max_value = np.argmax(yankees)
MIN_Y_VAL = 0
MAX_Y_VAL = np.max(yankees + cards)


ax1.plot(xaxis, yankees, label='Yankees', color=BLUE, marker='.', linestyle='--', linewidth=1.0)
ax1.plot(xaxis, cards, label='Cardinals', color=RED, marker='.', linewidth=1.0)
ax2.plot(xaxis, dbacks, label='Dbacks', color=GREEN, marker='.', linewidth=1.0)

ax1.fill_between(xaxis, yankees, cards,
                 where=(yankees > cards), color=BLUE,
                 interpolate=True, alpha=OPACITY,
                 label='Yankees above')
ax1.fill_between(xaxis, yankees, cards,
                 where=(yankees <= cards), color=RED,
                 interpolate=True, alpha=OPACITY,
                 label='Cards above')

# plt.annotate('Max', xy=(xaxis[max_value] + 1, max(yankees)), xytext=(200, 80),
#               arrowprops=dict(facecolor='black', shrink=0.9))

ax1.set_title(TITLE)

ax1.legend(loc='upper left')
ax1.grid(True, which='both', alpha=OPACITY)
ax1.set_ylabel(YLABEL)

ax2.legend(loc='upper left')
ax2.grid(True, which='both', alpha=OPACITY)
ax2.set_xlabel(XLABEL)
ax2.set_ylabel(YLABEL)

plt.xticks(xaxis)
plt.ylim(MIN_Y_VAL, MAX_Y_VAL)

plt.tight_layout()
plt.show()