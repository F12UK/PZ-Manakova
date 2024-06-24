def sum_squares(n):
  """
  Вычисляет сумму квадратов чисел от N до 2N.

  Args:
    n: Целое число больше 0.

  Returns:
    Сумма квадратов чисел.

  Raises:
    ValueError: Если n меньше или равно 0.
  """

  if n <= 0:
    raise ValueError("n должно быть больше 0")

  total = 0
  for num in range(n, 2 * n + 1):
    total += num * num
  return total

try:
  n = int(input("Введите целое число N (больше 0): "))
  sum_result = sum_squares(n)
  print(f"Сумма квадратов чисел от N до 2N: {sum_result}")
except ValueError as e:
  print(f"Ошибка: {e}")
