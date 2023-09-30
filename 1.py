import random

s = '+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

n = int(input('Введите длину пороля?'))
p = ''

for i in range(n):
    p += random.choice(s)
print(p)