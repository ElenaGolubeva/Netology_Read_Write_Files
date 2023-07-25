import os

name_file = os.listdir(path='Files')
count_str = {}
for i in name_file:
    with open('Files/' + i, encoding='utf-8') as f:
        h = f.readlines()
        count_str[i] = len(h)
        count_str_sort = sorted(count_str, key=count_str.get)

with open('result_file.txt', 'a', encoding='utf-8') as g:
    for j in count_str_sort:
        with open('Files/' + j, encoding='utf-8') as k:
            rez = k.readlines()
            g.write(j + '\n')
            g.write(str(len(rez)) + '\n')
            g.write(' '.join(rez) + '\n')
