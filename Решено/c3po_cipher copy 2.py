#!/usr/bin/python3
from math import isqrt, sqrt

flag = "OmWars{test_flag}"

c3po_sounds = ['pi', 'deep', 'peeppeepdreep',
              'tzeeep', 'zheep', 'brynbrynbrrrtrtrtrtrtrtr',
              'meew', 'gleee', 'nleee', 'zwee', 'free','e','i','fi']


def encrypt(plaintext):
    h = int(flag.encode().hex(), 16)
    s = pow(h,2)
    for sound in c3po_sounds:
        s -= int(sound.encode().hex(), 16)
    return s

# print(encrypt('plaintext'))

def digit_to_char(digit):
    if digit < 10:
        return str(digit)
    return chr(ord('a') + digit - 10)

def str_base(number,base):
    if number < 0:
        return '-' + str_base(-number, base)
    (d, m) = divmod(number, base)
    if d > 0:
        return str_base(d, base) + digit_to_char(m)
    return digit_to_char(m)


def decrypt(shifr):
    s = shifr                                   # число, которое возвращается из encrypt(), т.е. зашифрованная строка. Она была получена после вычитания всех звуков в цикле
    for sound in c3po_sounds:                   # делаю обратные действия, восстанавливаю изначальную строку s из encrypt
        s += int(sound.encode().hex(), 16)
    h = s ** 0.5                                # беру квадратный корень, что б получить число, которое лежало в h в encrypt
    h = str_base(s, 16)                         # тут пытаюсь преобразовать в уже нужную строку
    return bytes.fromhex(h)




h = int(flag.encode().hex(), 16)
s = pow(h,2)
for sound in c3po_sounds:                   # отняли
    s -= int(sound.encode().hex(), 16)

# --------REVERSE

# s1 = s
# s1 = 4029149106802270262261376333028168448385013546850298683812978107472482499330012076855563201168080728444698333165630056195537422690718301707185504928048146515598837784457344020789242249732551248197704206332545993656514078091470658230320663282257175317973446345620129467089453111895646563090539513900
s1 = 730493677738902302793947906425771100071392413079541618690800114244100988651501100
for sound in c3po_sounds:
    s1 += int(sound.encode().hex(), 16)     # вернули всё на место число s получено КАК ПОЛУЧИТЬ ИЗ НЕГО h? возвести в обратную степень не получается

# print(s1 == pow(h,2))                       # получилось Верно

# print(s1)

h1 = int(isqrt(s1))                         # Получил исходное число h
# h1 = sqrt(s1)

h1_o = str_base(h1, 16)
# print(h1_o)
print(bytes.fromhex(h1_o))

# s2 = s1 ** 0.5
# s2 = pow(s1, (1.0 / 2))
# s2 = sqrt(s1)

# print(h)
# print(pow(h, 2))
# print(int(s1 ** 0.5))
# print(h - int(pow(h, 2) ** (1/2)))
# res = str_base(int(pow(h, 2) ** (1/2))-659259867071000495429763, 16)
# print(bytes.fromhex(res))


def decrypt(c: int):
    '''
        Вглянув на функцию шифрования, можно понять,
        что флаг переводится в hex, из него в int,
        а далее вычитаются строки преобразованные также.

        Лист с строками нам дан, так что мы можем легко
        написать декрипт
    '''

    c = sum([c] + list(map(lambda s: int(s.encode().hex(), 16), c3po_sounds)))  # Перебираем строки и прибавляем к зашифрованному тексту

    # return bytes.fromhex(hex(isqrt(c))[2:]).decode()  # Берем из результата суммирования квадратный корень, переводим в строку
    return bytes.fromhex(hex(isqrt(c))[2:]).decode()

c = encrypt('s')

print(decrypt(c))