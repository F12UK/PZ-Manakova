def element_with_k_index(nums: list, k: int) -> list:
  """
  Функция для вывода элементов списка с индексами, кратными K.

  Args:
      nums: Список чисел.
      k: Целое число (1 < K < N).

  Returns:
      Список элементов с кратными K индексами.
  """
  try:
    # Проверка корректности K
    if k <= 1 or k >= len(nums):
      raise ValueError("K должно быть больше 1 и меньше длины списка.")

    result = [nums[i] for i in range(len(nums)) if i % k == 0]
    return result
  except ValueError as err:
    print(f"Ошибка: {err}")
    return []

# Пример использования
nums = [1, 2, 3, 4, 5]
k = 2
result = element_with_k_index(nums, k)
print(f"Элементы с индексами, кратными {k}: {result}")
