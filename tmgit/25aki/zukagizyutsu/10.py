# print(36/15)
# print(100/2.4)
# print(100/1.19)
# print(100/0.98)

# 又は
# print("a =", [i*i for i in range(8)])
# 又は,
 
x = 1
i = 1
a = [0] * 8
try:
    for _ in range(8):
        a[i] = i * i
        i = i+1
except IndexError as e:
    print("a =", a)
    print("i =", i)
    print(""" "error" """,e)


