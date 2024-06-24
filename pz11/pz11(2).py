def process_text_file(text18-10.txt):
  """
  Обрабатывает текстовый файл, выводит информацию и создает стихотворный файл.

  Args:
    filename: Имя файла.
  """
  try:
    with open(text18-10.txt, 'r') as f:
      text = f.read()

    upper_case_count = sum(letter.isupper() for letter in text)
    print(f"Содержимое файла:\n{text}")
    print(f"Количество букв в верхнем регистре: {upper_case_count}")

    # Преобразуем текст в стихотворную форму (простой пример)
    poem = "\n".join(text.split()[:4]) + "\n\n"
    poem += f"- Автор: Bard\n"
    poem += f"- Название: Стихотворение из {text18-10.txt}"

    with open(text18-10.txt + '.poem.txt', 'w') as f:
      f.write(poem)
  except Exception as e:
    print(f"Ошибка при обработке файла: {e}")

# Пример использования
process_text_file('text18-10.txt')
