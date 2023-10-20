import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
fig = plt.figure(figsize=(16,9))
ax1 = fig.add_subplot(311)
ax2 = fig.add_subplot(312)
ax3 = fig.add_subplot(313)
values1 = np.random.normal(0,10,100)
values2 = np.random.normal(0,10,1000)
values3 = np.random.normal(0,10,10000)
ax1.hist(values1,50)
ax2.hist(values2,50)
ax3.hist(values3,50)
plt.grid()
plt.show()