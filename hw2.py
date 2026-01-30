import numpy as np


# alcohol,volatile acidity,sulphates,pH,quality
dataset = np.loadtxt(
"wine_quality.csv",
delimiter=",",
skiprows=1, # пропускаем строку с названиями колонок
)
# dataset.shape -> (N, 5)
# Для удобства можно выделить колонки:

alcohol = dataset[:, 0]
volatile_acidity = dataset[:, 1]
sulphates = dataset[:, 2]
pH = dataset[:, 3]
quality = dataset[:, 4]


# task1

print(f"\ntask1:\n\nСреднее для каждого столбца - {alcohol.mean()},"
      f" {volatile_acidity.mean()},{sulphates.mean()},"
      f" {pH.mean()}, {quality.mean()}\n\n"
      
      f"Медиана каждого столбца - {np.median(alcohol)},"
      f" {np.median(volatile_acidity)},{np.median(sulphates)},"
      f" {np.median(pH)}, {np.median(quality)}\n\n"
      
      f"Дисперсия - {np.var(alcohol)},"
      f" {np.var(volatile_acidity)},{np.var(sulphates)},"
      f" {np.var(pH)}, {np.var(quality)}\n\n"
      
      f"Минимум - {np.min(alcohol)},"
      f" {np.min(volatile_acidity)},{np.min(sulphates)},"
      f" {np.min(pH)}, {np.min(quality)}\n\n"
      
      f"Максимум - {np.max(alcohol)},"
      f" {np.max(volatile_acidity)},{np.max(sulphates)},"
      f" {np.max(pH)}, {np.max(quality)}\n")


# task2

max_q = np.max(quality)
mask = [q == max_q for q in quality]
res_ph = pH[mask]
print(f"tsk2: Средний ph - {res_ph.mean()}")


# task3

min_q = quality.min()
max_q = quality.max()
quality_norm = (quality - min_q)/(max_q - min_q)
print(f"\ntask3: quality нормализована. "
      f"мин знач - {quality_norm.min()},"
      f" макс знач - {quality_norm.max()}.")

# task4

# dataset[:,0] = (dataset[:,0] - dataset[:,0].mean())/dataset[:,0].std()
# print(f"task4: {np.mean(dataset[:,0])}")
# print(np.std(dataset[:,0]))

# task5

mask = quality >= 7
res = dataset[mask]
print("\ntask5: ", res[:,0].mean())
print(res[:,4].mean())
print(mask.sum())

# task6

indexes = np.argsort(alcohol)[:5]
for i in indexes[::-1]:
      print("\ntask6: ", *dataset[i,(0,4)])

# task7

print("\ntask7:")
print((quality == np.min(quality)).sum())
print((quality == np.max(quality)).sum())
minn = np.mean(quality) - np.std(quality)
maxx = np.mean(quality) + np.std(quality)
print(np.sum((quality >= minn) & (quality <= maxx)))

# task8

alcohol_m = alcohol - alcohol.mean()
quality_m = quality - quality.mean()
print("\ntask 8:\n", np.dot(alcohol_m,quality_m))
len_alc = np.linalg.norm(alcohol_m)
len_qua = np.linalg.norm(quality_m)
print(np.dot(alcohol_m,quality_m)/(len_alc*len_qua))
# при увеличении алкоголя качествов среднем растёт