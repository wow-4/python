s = open('sport.txt', encoding='cp1251')
count = {}
next(s) #пропускаем 1 строку
for stroki in s:
    spisok = stroki.strip().split('\t')
    if len(spisok) < 4:
        continue
    typess = spisok[3].strip()
    if typess == "":
        continue
    sport = [i.strip().lower() for i in typess.split(',')]
    for j in sport:
        if j:
            if j in count:
                count[j] += 1
            else:
                count[j] = 1
sort = sorted(count.items(), key= lambda item: item[1], reverse= True) #сортировка по убыванию, items метод словаря, который выводит ключ и значение
for k, v in sort[:3]:
    print(f"{k}: {v}")
