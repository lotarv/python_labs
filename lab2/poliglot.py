all_langs = {}



amount_of_students = int(input("Введите число школьников:"))

for i in range(amount_of_students):
    print(f"***Студент {i + 1}***")
    langs_amount = int(input("Введите число языков:"))
    print("Вводите языки:")
    for j in range(langs_amount):
        lang = input()
        if lang in all_langs.keys():
            all_langs[lang] += 1
        else:
            all_langs[lang] = 1


all_know_count = 0
all_know_langs = []
for lang in all_langs.keys():
    if all_langs[lang] == amount_of_students:
        all_know_count += 1
        all_know_langs.append(lang) 
print("Количество языков, которые знают все школьники:", all_know_count)

print("Языки, которые все знают:")

for lang in sorted(all_know_langs):
    print(lang)


print("Число языков, что знает хотя бы один школьник: ", len(all_langs.keys()))

print("Список таких языков:")

for lang in sorted(all_langs.keys()):
    print(lang)





