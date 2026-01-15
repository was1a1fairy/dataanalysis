import numpy as np

print()
#task1
print()

temps = np.array([15.2, 16.8, 14.5, 17.0, 16.1])
print(np.sum(temps))
print(np.average(temps))
print(np.amax(temps))
print(np.amin(temps))

print()
# task2
print()

h1 = np.array([45, 50, 47])
h2 = np.array([48, 46, 52])
print(h1+h2,h1*h2,h1@h2)

print()
# task3
print()

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

print()
# task4
print()

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

print()
# task5
print()

ph = np.array([
    [7.1, 7.4, 7.0],
    [6.9, 7.2, 7.1],
    [7.3, 7.5, 7.2],
    [7.0, 7.1, 6.8],
    [6.8, 6.9, 6.7],
    [7.4, 7.6, 7.3]
])

print(ph.mean(axis=1))
print(ph.sum(axis=0))
print(ph.sum(axis=1))
print(ph.var(axis=0, ddof=1))


print()
# task6
print()

consumption = np.array([
[ 8, 6, 5], # Mon
[10, 7, 6], # Tue
[ 9, 8, 7], # Wed
[11, 10, 9], # Thu
[14, 12, 11], # Fri
[16, 15, 13], # Sat
[12, 11, 10] # Sun
])
days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
houses = ['H1','H2','H3']

print(consumption.sum(axis=0))
print(consumption.sum(axis=1))
print(consumption.mean(axis=0))
print([days[i] for i in consumption.argmax(axis=1)])
print(consumption.var(axis=0, ddof=1))

print()
# task7
print()

sensors = np.array([
[15, 101, 20, 0.5],
[16, 100, 21, 0.6],
[15, 102, 19, 0.4],
[17, 103, 22, 0.7],
[18, 104, 23, 0.6],
[19, 105, 24, 0.8],
[17, 103, 22, 0.5]], dtype=float)
types = ['TempSensor','PressureSensor','FlowSensor','VibrationSensor']

print(sensors.sum(axis=0))
print(sensors.mean(axis=0))
print(sensors.var(axis=0, ddof=1))
print(types[np.argmax(sensors.sum(axis=0))])