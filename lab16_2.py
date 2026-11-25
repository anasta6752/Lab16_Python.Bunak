
import matplotlib.pyplot as plt
from collections import Counter

# Український алфавіт
letters = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'

# Читання текстового файлу
with open('text.txt', 'r', encoding='utf-8') as file:
    text = file.read().lower()

# Підрахунок частоти літер
text_letters = [char for char in text if char in letters]
frequency = Counter(text_letters)

# Підготовка даних для гістограми
x = list(letters)
y = [frequency[letter] for letter in letters]

# Побудова гістограми
plt.figure(figsize=(14, 6))
plt.bar(x, y)

plt.xlabel('Українські літери')
plt.ylabel('Кількість повторень')
plt.title('Гістограма частот українських літер')
plt.grid(axis='y')

plt.show()
