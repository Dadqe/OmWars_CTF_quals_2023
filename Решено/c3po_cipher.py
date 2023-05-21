#!/usr/bin/python3


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


print(encrypt(flag))

# 4029149106802270262261376333028168448385013546850298683812978107472482499330012076855563201168080728444698333165630056195537422690718301707185504928048146515598837784457344020789242249732551248197704206332545993656514078091470658230320663282257175317973446345620129467089453111895646563090539513900

