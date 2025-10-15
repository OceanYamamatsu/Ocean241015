# a = int(input())
a = int(20596743834967217731323525323803952313616238702337354308363233353310617617650545138317671939264209492298243621150709975444649092424695197963762450352178818
)
b = 0
b2= a
c = 5
la = []
while b == 0:
    if a % 2 == 0:
        a //= 2
        la.append(2)
    elif a % 3 == 0:
        a //= 3
        la.append(3)
    else:
        while a >= c:
            if a % c == 0:
                a //= c
                la.append(c)
            else:
                c += 1
        break
la.append(a)

if len(la) == 2:
    print('素数')

else:
    print(la)