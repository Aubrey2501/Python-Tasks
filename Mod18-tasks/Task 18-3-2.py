text = input('Введите текст: ')
text_lst = text.split()
print(text_lst)
text_new = ' '.join(text_lst)

print('Исправленный текст:', text_new)