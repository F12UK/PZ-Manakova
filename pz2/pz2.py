def calculate_unoccupied_length(a, b):
  """
  Функция вычисляет длину незанятой части отрезка A, 
  если на нем разместить максимально возможное количество 
  отрезков длины B без наложений.

  Args:
      a: Целое положительное число, длина отрезка A.
      b: Целое положительное число, длина отрезка B (B < A).

  Returns:
      Целое число, длина незанятой части отрезка A.
  """

  try:
    # Проверка входных данных
    if not isinstance(a, int) or not isinstance(b, int):
      raise TypeError("Ожидаются целые числа для A и B")
    if a <= 0 or b <= 0:
      raise ValueError("A и B должны быть больше 0")
    if b >= a:
      raise ValueError("B должно быть меньше A")

    # Вычисление количества отрезков
    number_of_segments = a // b

    # Вычисление длины незанятой части
    unoccupied_length = a % b

    return unoccupied_length

  except TypeError as e:
    print(f"Ошибка типа: {e}")
    return None
  except ValueError as e:
    print(f"Ошибка значения: {e}")
    return None

# Пример использования
a = 10
b = 3

unoccupied_length = calculate_unoccupied_length(a, b)
print(f"Длина незанятой части отрезка: {unoccupied_length}")
