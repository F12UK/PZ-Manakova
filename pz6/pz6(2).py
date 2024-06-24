def count_monotonic_ranges(nums: list) -> int:
  """
  Функция для подсчета монотонных промежутков в списке.

  Args:
      nums: Список чисел.

  Returns:
      Количество монотонных промежутков.
  """
  if not nums:
    return 0

  direction = None  # Направление (None, 1 - возрастает, -1 - убывает)
  count = 1  # Количество монотонных промежутков

  for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
      if direction == -1:
        count += 1
      direction = 1
    elif nums[i] < nums[i - 1]:
      if direction == 1:
        count += 1
      direction = -1

  return count

# Пример использования
nums = [1, 2, 6, 4, 5, 3]
count = count_monotonic_ranges(nums)
print(f"Количество монотонных промежутков: {count}")
