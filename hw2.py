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
      f" {np.max(pH)}, {np.max(quality)}\n\n")