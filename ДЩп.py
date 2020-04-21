from math import log2


def is_int(s):
    s *= 10
    if s % 10 == 0:
        return True
    else:
        return False


x = int(input())

if x == 0 or x == 1:
    print("Нет")
elif is_int(log2(x)):
    print(log2(x))
else:
    print("Нет")
# кукуха поехала

