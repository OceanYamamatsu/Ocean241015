patterns = [format(i, '06b') for i in range(64)]
print(patterns)
for u in patterns:
    print(u)
nedan=[120,170,40,200,350,80]
ans=[]
for u in patterns:
    ct=-1
    an=0
    for i in u:
        ct+=1
        if i == 1:
            an+=nedan[ct]
    else:
        ans.append([u,an])

print(ans)