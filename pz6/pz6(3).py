def cyclic_shift_right(nums: list) -> None:
  """
  Функция для циклического сдвига списка вправо с обнулением первого элемента.

  Args:
      nums: Список чисел.
  """
  if not nums:
    return

  try:
    # Проверка возможности выполнения сдвига
    if len(nums) == 1:
      raise ValueError("Сдвиг в списке с одним элементом невозможен.")

    # Сдвиг вправо
    last_element = nums.pop()
    nums.insert(0, 0)
  except ValueError as err:
    print(f"Ошибка: {err}")

# Пример использования
nums = [1, 2, 3, 4]
cyclic_shift_right(nums)
print(f"Список после циклического сдвига: {nums}")
