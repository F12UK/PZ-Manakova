def zamena_elementov(matrica, massiv):
  """
  Заменяет элементы третьей строки матрицы элементами из одномерного массива.

  Args:
    matrica: Список списков, представляющий собой матрицу.
    massiv: Список, элементы которого будут использованы для замены.

  Returns:
    Обновленная матрица.
  """
  if len(massiv) != len(matrica[2]):
    raise ValueError("Размер массива должен соответствовать длине третьей строки матрицы.")

  matrica[2] = massiv

  return matrica

# Пример использования
matrica = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
massiv = [10, 11, 12]

matrica_obnovlennaya = zamena_elementov(matrica.copy(), massiv.copy())
print(matrica_obnovlennaya)  # [[1, 2, 3], [4, 5, 6], [10, 11, 12]]
