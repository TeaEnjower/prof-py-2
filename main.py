from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re

with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

phone = []
for i in contacts_list:
  name = i[:3]
  name = " ".join(name)
  name = name.split(" ")
  i[0] = name[0]
  i[1] = name[1]
  i[2] = name[2]
  
  pattern = r'(\+7|8)\s*\(*(\d\d\d)\)*\s*\-*(\d\d\d)\s*\-*(\d\d)\s*\-*(\d\d)\s*(?:\(*(доб.) (\d\d\d\d)\)*)?'      #+7(999)999-99-99 r'(\+7|8)\s*\(*\d\d\d\)*\s*\-*\d\d\d\s*\-*\d\d\s*\-*\d\d\s*'
  result = re.sub(pattern, r"+7(\2)\3-\4-\5 \6\7", i[5])
  i[5] = result
pprint(contacts_list)

#print(phone)
# TODO 1: выполните пункты 1-3 ДЗ
# ваш код



# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(contacts_list)