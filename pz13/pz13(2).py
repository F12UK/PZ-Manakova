def srednee_arifmeticheskoe_polozhitelnih(matrica):
  """
  Находит среднее арифметическое положительных элементов матрицы.

  Args:
    matrica: Список списков, представляющий собой матрицу.

  Returns:
    Среднее арифметическое положительных элементов.
  """
  srednee = 0
  kolvo_polozhitelnih = 0

  for stroka in matrica:
    for element in stroka:
      if element > 0:
        srednee += element
        kolvo_polozhitelnih += 1

  if kolvo_polozhitelnih == 0:
    return None

  return srednee / kolvo_polozhitelnih

# Пример использования
matrica = [[1, 2, -3], [4, 5, -6], [7, -8, 9]]

srednee = srednee_arifmeticheskoe_polozhitelnih(matrica.copy())
print(srednee)  # 5.333333333333333