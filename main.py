spis=input("Введите строку для определения длины, кол-ва гласных и согласных:")
gls = 0
sgl = 0
length = 0
vse_gls = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
vse_sgl = "бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ"
for char in spis:#цикл for
    length += 1
    if char in vse_gls:
        gls += 1
    elif char in vse_sgl:
        sgl += 1


print('Количество гласных:',gls)
print('Количество согласных:',sgl)
print('Длина строки:',length)