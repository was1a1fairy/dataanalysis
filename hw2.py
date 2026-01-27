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

print(f"\nСреднее для каждого столбца - {alcohol.mean()},"
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
print(f"task3: quality нормализована. мин знач - {quality_norm.min()}, макс знач - {quality_norm.max()}.")