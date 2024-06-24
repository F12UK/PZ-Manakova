def generate_numbers_file(filename, numbers):
  """
  Создает текстовый файл с последовательностью чисел.

  Args:
    filename: Имя файла.
    numbers: Список чисел.
  """
  try:
    with open(filename, 'w') as f:
      for num in numbers:
        f.write(f"{num}\n")
  except Exception as e:
    print(f"Ошибка при создании файла: {e}")

def process_numbers_file(input_filename, output_filename):
  """
  Обрабатывает текстовый файл с числами и создает новый файл с результатами.

  Args:
    input_filename: Имя входного файла.
    output_filename: Имя выходного файла.
  """
  try:
    with open(input_filename, 'r') as f:
      numbers = [int(num) for num in f.readlines()]

    reversed_numbers = numbers[::-1]
    second_half_sum = sum(reversed_numbers[len(numbers) // 2:])

    with open(output_filename, 'w') as f:
      f.write(f"Количество элементов: {len(numbers)}\n")
      f.write(f"Элементы в обратном порядке: {reversed_numbers}\n")
      f.write(f"Сумма элементов последней половины: {second_half_sum}\n")
  except Exception as e:
    print(f"Ошибка при обработке файла: {e}")

# Пример использования
numbers = [10, -5, 2, 0, -7, 3]
generate_numbers_file('numbers.txt', numbers)
process_numbers_file('numbers.txt', 'processed_numbers.txt')
