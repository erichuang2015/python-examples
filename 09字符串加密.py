#!/usr/bin/env python3
# coding:utf-8


# s = 'The Zen of Python'
# for c in s:
#     if 65 <= ord(c) <= 90:
#         c = chr(ord(c) + 13 if ord(c) + 13 <= 90 else ord(c) + 13 - 90 + 64)
#     elif 97 <= ord(c) <= 122:
#         c = chr(ord(c) + 13 if ord(c) + 13 <= 122 else ord(c) + 13 - 122 + 96)
#     print(c, end='')


# str_src = 'The Zen of Python'
# str_dst = ''
# for c in str_src:
#     if 65 <= ord(c) <= 90:
#         c = chr((ord(c) - 65 + 13) % 26 + 65) # 注意用%的思想，循环的都可以用%
#     elif 97 <= ord(c) <= 122:
#         c = chr((ord(c) - 97 + 13) % 26 + 97)
#     str_dst += c
# print(str_dst)


s1 = '''The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!'''

s2 = '''Gur Mra bs Clguba, ol Gvz Crgref

Ornhgvshy vf orggre guna htyl.
Rkcyvpvg vf orggre guna vzcyvpvg.
Fvzcyr vf orggre guna pbzcyrk.
Pbzcyrk vf orggre guna pbzcyvpngrq.
Syng vf orggre guna arfgrq.
Fcnefr vf orggre guna qrafr.
Ernqnovyvgl pbhagf.
Fcrpvny pnfrf nera'g fcrpvny rabhtu gb oernx gur ehyrf.
Nygubhtu cenpgvpnyvgl orngf chevgl.
Reebef fubhyq arire cnff fvyragyl.
Hayrff rkcyvpvgyl fvyraprq.
Va gur snpr bs nzovthvgl, ershfr gur grzcgngvba gb thrff.
Gurer fubhyq or bar-- naq cersrenoyl bayl bar --boivbhf jnl gb qb vg.
Nygubhtu gung jnl znl abg or boivbhf ng svefg hayrff lbh'er Qhgpu.
Abj vf orggre guna arire.
Nygubhtu arire vf bsgra orggre guna *evtug* abj.
Vs gur vzcyrzragngvba vf uneq gb rkcynva, vg'f n onq vqrn.
Vs gur vzcyrzragngvba vf rnfl gb rkcynva, vg znl or n tbbq vqrn.
Anzrfcnprf ner bar ubaxvat terng vqrn -- yrg'f qb zber bs gubfr!'''

# 因为13正好是26的一半，所以可以互相转换，而不用改代码
d = {}
for c in (65, 97):
    for i in range(26):
        d[chr(c+i)] = chr((i+13) % 26 + c)
print(''.join([d.get(c, c) for c in s2]))
