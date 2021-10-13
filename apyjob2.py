from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re
from collections import defaultdict

with open("phonebook_raw.csv", encoding='utf8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код
con_dic = defaultdict()
del_list = []
linenum = 0
for lin in contacts_list:
    t_lin = str(lin[0]).strip().split()
    lt_lin = len(t_lin)
    if lt_lin == 1:
        t_lin2 = str(lin[1]).strip().split()
        lt_lin2 = len(t_lin2)
        if lt_lin2 == 2:
            lin[2] = t_lin2[1]
            lin[1] = t_lin2[0]
    elif lt_lin == 2:
        if lin[1]:
            lin[2] = lin[1]
        lin[1] = t_lin[1]
        lin[0] = t_lin[0]
    elif lt_lin == 3:
        lin[2] = t_lin[2]
        lin[1] = t_lin[1]
        lin[0] = t_lin[0]
    ver_key = lin[0] + lin[1]
    if ver_key in con_dic.keys():
        lineno = con_dic[ver_key]
        del_list.append(linenum)
        for i in range(3, len(lin)):
            if lin[i]:
                contacts_list[lineno][i] = lin[i]
    else:
        con_dic[ver_key] = linenum
    linenum += 1

for i in sorted(del_list, reverse=True):
    contacts_list.pop(i)

phone_pat = r'(?:\+7|8)\D*(\d{3})\D*(\d+)\D*(\d{2})\D*(\d{2})(?:\D*(\d*))'
phone_com = re.compile(phone_pat)
for lin in contacts_list:
    t_ph = phone_com.match(lin[5])
    if t_ph:
        g1, g2, g3, g4, g5 = t_ph.groups()
        temp_phone_s = f'+7 ({g1}) {g2}-{g3}-{g4}'
        if g5:
            temp_phone_s += f' доб. {g5}'
        lin[5] = temp_phone_s
# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook_n.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts_list)
