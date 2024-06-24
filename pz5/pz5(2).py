def Minmax(X, Y):
  """Функция, записывающая в X минимум, а в Y - максимум из X и Y."""
  if X < Y:
    Y, X = X, Y
  return X, Y

# Пример использования:
A = float(input("Введите A: "))
B = float(input("Введите B: "))
C = float(input("Введите C: "))
D = float(input("Введите D: "))

min_val, max_val = Minmax(A, B)
min_val, max_val = Minmax(min_val, C)
min_val, max_val = Minmax(min_val, D)

print(f"Минимальное значение: {min_val}")
print(f"Максимальное значение: {max_val}")
