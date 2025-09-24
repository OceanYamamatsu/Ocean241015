i = 0
while True:
    bin_str = format(i, '04b')
    print(bin_str)
    if bin_str == '1111':
        break
    print(i)
    i += 1
print(i+1)
