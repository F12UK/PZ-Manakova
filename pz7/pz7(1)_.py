def reverse_string(string):
  """
  Функция переворачивает заданную строку.

  Args:
    string (str): Исходная строка.

  Returns:
    str: Перевернутая строка.
  """
  try:
    if not isinstance(string, str):
      raise TypeError("Входные данные должны быть строкой.")
    return string[::-1]
  except TypeError as e:
    print(f"Ошибка типа: {e}")
  except Exception as e:
    print(f"Неожиданная ошибка: {e}")

# Пример использования
original_string = "Привет!"
reversed_string = reverse_string(original_string)
print(f"Исходная строка: {original_string}")
print(f"Перевернутая строка: {reversed_string}")
