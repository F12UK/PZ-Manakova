import re

def find_last_names_with_initials(filename):
  """
  Функция для поиска фамилий с инициалами в текстовом файле.

  Args:
    filename: Строка, содержащая имя файла.

  Returns:
    Список строк, содержащих фамилии с инициалами.
  """

  with open(filename, 'r', encoding='utf-8') as f:
    text = f.read()

  # Регулярное выражение для поиска фамилий с инициалами
  pattern = r'\b[А-ЯЁа-я]+\.\s*[А-ЯЁа-я]+\.'

  # Поиск совпадений
  matches = re.findall(pattern, text)

  return matches

if __name__ == '__main__':
  # Укажите имя файла
  filename = 'Dostoevsky.txt'

  # Вызов функции и вывод результатов
  last_names_with_initials = find_last_names_with_initials('C:/Users/your_username/Documents/Dostoevsky.txt')
  print(f'Найденные фамилии с инициалами: {last_names_with_initials}')