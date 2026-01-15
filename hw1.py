import numpy as np

#task1
temps = np.array([15.2, 16.8, 14.5, 17.0, 16.1])
print(np.sum(temps))
print(np.average(temps))
print(np.amax(temps))
print(np.amin(temps))

# task2

h1 = np.array([45, 50, 47])
h2 = np.array([48, 46, 52])
print(h1+h2,h1*h2,h1@h2)