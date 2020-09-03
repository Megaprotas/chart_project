from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from collections import Counter

plt.style.use('fivethirtyeight')

TITLE = 'Bar chart 2'
XLABEL = 'Counter'
YLABEL = 'Movie'
OPACITY = 0.3

data = pd.read_csv('data2.csv')
ids = data['ids']
movies = data['movies']

movies_counter = Counter()

for movie in movies:
    movies_counter.update(movie.split(';'))

movies_final = []
top = []

for item in movies_counter.most_common(5):
    movies_final.append(item[0])
    top.append(item[1])

movies_final.reverse()
top.reverse()

plt.xlabel(XLABEL)
plt.ylabel(YLABEL)

plt.title(TITLE)
plt.grid(True, which='both', alpha=OPACITY)

plt.tight_layout()
plt.barh(movies_final, top)
plt.show()