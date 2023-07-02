from lang import detect

file = input("Введи назву файлу:")
with open(file, 'r', encoding='utf-8') as f:
    text = f.read()

language = detect(text)
print(f"Текст файлу: {text}")
print(f"Виявлена мова: {language}")