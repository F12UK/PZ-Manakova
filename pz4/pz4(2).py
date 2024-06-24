def find_max_k(n):
  """
  Находит наибольшее K, при котором 3K < N.

  Args:
    n: Целое число больше 1.

  Returns:
    Наибольшее K.

  Raises:
    ValueError: Если n меньше или равно 1.
  """

  if n <= 1:
    raise ValueError("n должно быть больше 1")

  k = 0
  while 3 * k < n:
    k += 1
  return k - 1

try:
  n = int(input("Введите целое число N (больше 1): "))
  max_k = find_max_k(n)
  print(f"Наибольшее K, при котором 3K < N: {max_k}")
except ValueError as e:
  print(f"Ошибка: {e}")
