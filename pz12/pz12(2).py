import string

def extract_digits(text):
  """
  Функция для извлечения цифр из строки с обработкой исключений.

  Args:
    text: Строка, из которой нужно извлечь цифры.

  Returns:
    Строку, содержащую только цифры из исходной строки.
  """
  try:
    digits = ""
    for char in text:
      if char in string.digits:
        digits += char
    return digits
  except TypeError:
    print("Ошибка: тип данных не поддерживается. Строка должна быть типа str.")

# Пример использования
try:
  text = "TheGreatPyramidofKhufuatGizawasbuiltabout2700BC,755feet(230metres)longand481feet(147metres)high."

  extracted_digits = extract_digits(text)
  print(f"Цифры из строки: {extracted_digits}")
except Exception as e:
  print(f"Произошла ошибка: {e}")
