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

# task3

x = np.array([
    [20.1, 20.3, 19.8],
    [21.0, 20.7, 20.2],
    [19.5, 19.8, 19.3],
    [20.8, 21.1, 20.6]
])

print(np.mean(x,axis=0))
print(np.sum(x,axis=1))
print(np.var(x,axis=0,ddof=1))
print(np.argmin(np.var(x,axis=0,ddof=1)))

# task4

z = np.array([
    [20.1, 20.3, 19.8],
    [21.0, 20.7, 20.2],
    [19.5, 19.8, 19.3],
    [20.8, 21.1, 20.6]
])

col_min = np.min(z,axis=0)
col_max = np.max(z,axis=0)
col_range = col_max - col_min
print(col_range)
print((z - col_min)/col_range)
print(np.sum(((z - col_min)/col_range), axis=0))