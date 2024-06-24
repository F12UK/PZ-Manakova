def countdown(num):
  """Функция, решающая задачу с итеративным вычитанием цифр."""
  count = 0
  while num > 0:
    sum_digits = sum(int(el) for el in str(num))
    num -= sum_digits
    count += 1
  return count

# Пример использования:
try:
  number = int(input("Введите число: "))
  if number < 0:
    raise ValueError("Число должно быть неотрицательным")
  result = countdown(number)
  print(f"Для получения нуля потребовалось {result} итераций.")
except ValueError as err:
  print(err)
