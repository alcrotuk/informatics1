import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

f = pd.read_csv('iris_data.csv')
x = list(f['PetalLengthCm'])
y = list(f['Species'])
c1 = 0
c2 = 0
c3 = 0
b1 = 0  # Iris-setosa
b2 = 0  # Iris-versicolor
b3 = 0  # Iris-virginica
for i in x:
    if i < 1.2:
        c1 += 1
    elif i > 1.5:
        c3 += 1
    else:
        c2 += 1
for i in y:
    if i == 'Iris-setosa':
        b1 += 1
    elif i == 'Iris-versicolor':
        b2 += 1
    else:
        b3 += 1
fig = plt.figure(figsize=(16, 9))
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)
ax1.pie([c1 / len(x), c2 / len(x), c3 / len(x)], labels=['l<1.2', '1.2<=l<=1.5', '1.5<l'])
ax2.pie([b1 / len(y), b2 / len(y), b3 / len(y)], labels=['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'])
ax1.set_title('длины лепестков')
ax2.set_title('виды ирисов')
plt.show()