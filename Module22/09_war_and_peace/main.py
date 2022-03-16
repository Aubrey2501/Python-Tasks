import zipfile
archive = 'voyna-i-mir.zip'
with zipfile.ZipFile(archive, 'r') as zip_file:
    zip_file.extractall('txt_file')
zip_file.close()

txt_file = open('txt_file/voyna-i-mir.txt', 'r', encoding='utf-8')
book = txt_file.read()
txt_file.close()

book_lst = book.split()
book_lst_txt = ''.join(book_lst)

sym_dict = dict()

for i_sym in book_lst_txt:
    if i_sym.isalpha() and i_sym not in sym_dict:
        sym_dict[i_sym] = book_lst_txt.count(i_sym)

sort_dict = sorted(sym_dict.items(), key=lambda x: x[1], reverse=True)
for i, i_elem in sort_dict:
    print(i, ':', i_elem)

# зачет!
