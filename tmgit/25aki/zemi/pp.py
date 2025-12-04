# print(100*13**3*1)
# print(100*44**2*1)
# print(100*45**2*1)

print(100*13**3*1)
a=0

for i in range(3):
    a+=100*13
print(a)

count = 0
for i in range(13):
    for j in range(100 * 44):
        # a の処理
        count += 1

print(count)  # → 57200
print(13*100*44)
print('EEE')
print(2*1*100*44)
print(2*1*100*30)
print(2*1*100*10)
