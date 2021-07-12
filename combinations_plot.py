from matplotlib import pyplot as plt
import math
import numpy as np
plt.figure()
k = 2
n = 40
x = range(k, n)
y = []
y2 = []
for i in x:
    fact = math.factorial(i)
    y.append(i*i)

    y2.append(i*(i-1)/2)

plt.title('Combinations complexity O(n^2) and O(n(n-1)/2)')
plt.xlabel('(n) set size')
plt.ylabel('Complexity')
plt.plot(x, y, '.', color="#11bb64")
plt.plot(x, y2, '.')
plt.legend(['n^2', 'n(n-1)/2'])
plt.show()
