st = input('Введите строку ')
sim = input('Введите символ ')
k = 0	
for nom in range(len(st)): 

    if st[nom] == sim:
        k = k + 1

if k > 0:
    print('Заданный символ встречается в строке', k, 'раз')
else:
    print('Такого символа нет')
