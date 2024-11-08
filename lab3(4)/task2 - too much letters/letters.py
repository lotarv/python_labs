#Даны файл, содержащий текст на русском языке, и некоторые 
#буквы. Найти слово, содержащее наибольшее количество указанных букв.

with open("./file.txt", encoding="utf-8") as f:
    text = f.read()
    words = text.split(" ")

letter = input("Укажите букву: ")
word_much_letters = ""
for word in words:
    if word.lower().count(letter) > word_much_letters.lower().count(letter):
        word_much_letters = word


print(f"Слово с наибольшим количеством букв '{letter}': {word_much_letters}")


