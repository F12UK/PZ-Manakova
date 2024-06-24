def check_odd(a, b):
  """
  Проверяет, является ли ровно одно из чисел A и B нечетным.

  Args:
      a: Целое число.
      b: Целое число.

  Returns:
      bool: True, если ровно одно из чисел A и B нечетное, False - иначе.
  """
  try:
    # Проверить типы данных a и b
    if not isinstance(a, int) or not isinstance(b, int):
      raise TypeError("Ожидается два целых числа.")
    
    # Проверить четность чисел
    is_a_odd = a % 2 != 0
    is_b_odd = b % 2 != 0
    
    # Вернуть True, если ровно одно из чисел нечетное
    return is_a_odd ^ is_b_odd
  except TypeError as e:
    print(f"Ошибка: {e}")
    return False

# Пример использования
a = 3
b = 4
print(f"Проверка четности: {a} и {b} - {check_odd(a, b)}")
