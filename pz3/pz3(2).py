def get_days_in_month(month):
  """
  Определяет количество дней в месяце (невисокосного года).

  Args:
      month: Целое число от 1 до 12 (месяц).

  Returns:
      int: Количество дней в месяце.
  """
  try:
    # Проверить тип данных month
    if not isinstance(month, int):
      raise TypeError("Ожидается целое число от 1 до 12 (месяц).")
    
    # Проверить диапазон month
    if month < 1 or month > 12:
      raise ValueError("Недопустимое значение месяца.")
    
    # Определить количество дней в месяце
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return days_in_month[month - 1]
  except (TypeError, ValueError) as e:
    print(f"Ошибка: {e}")
    return None

# Пример использования
month = 2
print(f"Количество дней в феврале: {get_days_in_month(month)}")
