# Напишите программу, которая принимает на вход список слов такого вида:
# words = ["Speak ","to", "me ", "of", "Florence" ,"And ", "of", "the",
# "Renaissance"] а возвращает список
# words_clean = ["speak", "to", "me", "of", "florence", "and", "of", "the",
# "renaissance"]
# Другими словами, программа убирает пробелы в словах и приводит все слова к
# нижнему регистру.
# Подсказка: запросите help() по методам strip() и lower().


def clean_words(words):
    words_clean = []
    for word in words:
        word_clean = word.strip().lower()
        words_clean.append(word_clean)
    return words_clean


# Пример использования программы
words = ["Speak ", "to", "me ", "of", "Florence", "And ", "of", "the",
         "Renaissance"]
words_clean = clean_words(words)
print(words_clean)
