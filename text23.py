import string
f = open('text2323.txt', encoding = 'UTF8')
text = f.read()
f.close()
# Задание первое
not_sings = text.replace(',','').replace('.','').replace('!','').replace('?','').replace('«','').replace('«','').replace('»','').replace('—','')
# print(not_sings)
# Задание второе
list_not_sings = not_sings.split()
# print(list_not_sings)
# Задание третье
lower_list = list(map(lambda x:x.lower(),list_not_sings))
# Задание четвертое
set_text = set(lower_list)
temp = {}
for el in set_text:
    temp[el] = lower_list.count(el)
# print(temp)
# задание пятое
listdi = list(temp.items())
listdi.sort(key=lambda i:i[1],reverse=True)
print(listdi[:5])