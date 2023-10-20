import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
x = [1, 1.5, 2, 2.5, 3]
F = [3, 4.5, 6, 7.5, 9]
plt.figure(figsize=(16,9))
plt.plot(x, F, 'k', label = 'F(x)')
plt.title('зависимость силы упругости от растяжения', fontdict={'fontname' :'sans-serif' ,'fontsize': 20})
plt.grid()
plt.xlabel('растяжение пружины')
plt.ylabel('сила упругости')
plt.show()