# Задача 27.
# Пользователь вводит текст(строка). Словом считается 
# последовательность непробельных символов идущих 
# подряд, слова разделены одним или большим числом 
# пробелов. Определите, сколько различных слов 
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells

# str_1 = '''She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells'''.lower()
# str_1 = set(str_1.split())
# print(len(str_1))

print(len(set(input("input text: ").lower().split())))