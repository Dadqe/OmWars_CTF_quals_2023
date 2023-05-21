#!/usr/bin/python3


flag = "OmWars{test_flag}"

c3po_sounds = ['pi', 'deep', 'peeppeepdreep',
              'tzeeep', 'zheep', 'brynbrynbrrrtrtrtrtrtrtr',
              'meew', 'gleee', 'nleee', 'zwee', 'free','e','i','fi']


def encrypt(plaintext):
    h = int(flag.encode().hex(), 16)
    print(h)
    s = pow(h,2)
    for sound in c3po_sounds:
        s -= int(sound.encode().hex(), 16)
    return s


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

# print(type(encrypt(flag)))

# print(f"ITOG: {str(decrypt(encrypt(1)))}")



# Проверяю алгоритм обратного цикла, т.е. прибавления звуков

h = int(flag.encode().hex(), 16)
s = pow(h,2)
# print(f"s before sub: {s}")

s1 = s
for sound in c3po_sounds:
    s1 -= int(sound.encode().hex(), 16)
# print(f"s past sub: {s1}")

s2 = s1
for sound in c3po_sounds:
    s2 += int(sound.encode().hex(), 16)
# print(f"s pas calc: {s2}")

print(s2 == s)      # значит прибавление правильный метод

ishodnaya_stroka = str_base(h, 16)
# print(ishodnaya_stroka)




# flag_ish = pow(int(flag.encode().hex(), 16), 2)

# print(flag_ish)

# после int(hex(), 16 как получить снова строку хекса)

# print(encrypt(flag))

# 4029149106802270262261376333028168448385013546850298683812978107472482499330012076855563201168080728444698333165630056195537422690718301707185504928048146515598837784457344020789242249732551248197704206332545993656514078091470658230320663282257175317973446345620129467089453111895646563090539513900



# Тут я проверил декодирование после int(hex(), 16) ОСТАЛОСЬ узнать как сделать обратное действие hex()
h_was = flag.encode().hex()
h = int(flag.encode().hex(), 16)
h_back = str_base(h, 16)

# print(h_was)    # Это всё строки. Надо из них получить число, которое получалось при encode(), т.е. надо обратить действие метода hex()
# print(h)
# print(h_back)   # Это всё строки. Надо из них получить число, которое получалось при encode(), т.е. надо обратить действие метода hex()

# print(h_was == h_back)

a = flag.encode()   # <class 'bytes'>
print(a, type(a))

a_hex = a.hex()     # <class 'str'>
print(a_hex, type(a_hex))

# Из строки получаю байтовую строку
b = bytes.fromhex(a_hex)
print(b)

