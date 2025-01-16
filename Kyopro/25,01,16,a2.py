n=int(input())
a=list(set(map(int,input().split())))
print(a)
n=len(a)
ue=0
si=0
atama=a[-1]
karada=0
ct=0
ans=[]
bb=0
for i in range(n):
    atama=a[(n-1)-i]
    karada=a[(n-1)-i]
    while atama >= karada/2:
        ue+=1
        if 0 != (n-1)-ue:
            atama=a[(n-1)-ue]
        else:
            bb=1
            break
        ans.append(n-ue)
    else:
        print('w1',ue,n-ue)
    if bb==1:
        break
else:
    print('f1')
print(ans)
print(sum(ans))




n=int(input())
a=list((map(int,input().split())))
print(a)
ue=0
si=0
atama=a[-1]
karada=0
ct=0
ans=[]
bb=0
for i in range(n):
    atama =a[(n-1-1)-i]
    karada=a[(n-1)-i]
    while atama >= karada/2:
        if 0 != (n-1)-ue:
            atama=a[(n-1)-ue]
        else:
            bb=1
            break
        ue+=1
    else:
        ans.append(n-ue)
        print('w1',ue,n-ue)
    if bb==1:
        break
else:
    print('f1')
print(ans)
print(sum(ans))



n=int(input())
a=list((map(int,input().split())))
print(a)
ue=1
si=0
atama=a[n-2]
ct=0
ans=[]
bb=0
for i in range(n):
    karada=a[(n-1)-i]
    ct=0
    while atama > karada/2:
        if 0 <= ((n-1)-ue-ct):
            print((n-1)-ue-ct)
            print('n',n,'ue',ue,'ct',ct)
            atama=a[(n-1)-ue-ct]
            
        else:
            bb=1#break01
            break
        ct+=1
    else:
        ans.append(n-ue)
        print('apend','n',n,'ue',ue,'ct',ct)
        print('w1',(karada,atama),ue+ct,n-1-ue,'ans=',n-ue)
    if bb==1:#break01
        break
    ue+=1
else:
    print('f1')
print(ans)
print(sum(ans))