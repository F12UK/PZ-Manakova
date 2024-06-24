import os

def get_last_directory(file_path):
  """
  Функция извлекает имя последнего каталога из полного пути к файлу.

  Args:
    file_path (str): Полный путь к файлу.

  Returns:
    str: Имя последнего каталога.
  """
  try:
    if not isinstance(file_path, str):
      raise TypeError("Входные данные должны быть строкой.")
    head, tail = os.path.split(file_path)
    return tail or "\\"
  except TypeError as e:
    print(f"Ошибка типа: {e}")
  except Exception as e:
    print(f"Неожиданная ошибка: {e}")

# Пример использования
file_path1 = "C:\\Users\\user\\Documents\\example.txt"
file_path2 = "C:\\Users\\user\\Downloads\\"
last_directory1 = get_last_directory(file_path1)
last_directory2 = get_last_directory(file_path2)
print(f"Имя последнего каталога для {file_path1}: {last_directory1}")
print(f"Имя последнего каталога для {file_path2}: {last_directory2}")
