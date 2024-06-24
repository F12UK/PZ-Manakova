def negative_max(nums):
  """
  Функция для поиска максимального отрицательного числа в списке с обработкой исключений.

  Args:
    nums: Список целых чисел.

  Returns:
    Максимальное отрицательное число, или None, если нет отрицательных чисел.
  """
  try:
    negative_max = None
    for num in nums:
      if num < 0:
        if negative_max is None or num > negative_max:
          negative_max = num
    return negative_max
  except TypeError:
    print("Ошибка: список должен содержать только целые числа.")

def even_nums(nums):
  """
  Функция для поиска элементов, кратных 2, в списке с обработкой исключений.

  Args:
    nums: Список целых чисел.

  Returns:
    Список элементов, кратных 2.
  """
  try:
    even_nums = []
    for num in nums:
      if num % 2 == 0:
        even_nums.append(num)
    return even_nums
  except TypeError:
    print("Ошибка: список должен содержать только целые числа.")

def sum_of_evens(nums):
  """
  Функция для вычисления суммы элементов, кратных 2, в списке с обработкой исключений.

  Args:
    nums: Список целых чисел.

  Returns:
    Сумму элементов, кратных 2.
  """
  try:
    sum_of_evens = 0
    for num in even_nums(nums):
      sum_of_evens += num
    return sum_of_evens
  except TypeError:
    print("Ошибка: список должен содержать только целые числа.")

# Пример использования
try:
  nums = [1, 2, -3, 4, -5, 6]

  max_negative = negative_max(nums)
  print(f"Максимальное отрицательное число: {max_negative}")

  even_numbers = even_nums(nums)
  print(f"Элементы, кратные 2: {even_numbers}")

  sum_even = sum_of_evens(nums)
  print(f"Сумма элементов, кратных 2: {sum_even}")
except Exception as e:
  print(f"Произошла ошибка: {e}")
