import random


paroli =  "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
paroo = int(input('введите пароль: '))
vafl = ''

for i in range(paroo):
    vafl += random.choice(paroli)
print(vafl)
    