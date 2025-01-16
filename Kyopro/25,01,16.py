h,w,d=map(int,input().split())
men=[]
seen=[]
for i in range(h):
    seen.append([])
    xx=list(input())
    men.append(xx)
    ct=-1
    for q in xx:
        ct+=1
        if q =='H':
            seen[0].append([i,ct])
            xx[ct]=0
# print(seen)
ir,id,il,iu=0,1,2,3
idou=[[0,1],[1,0],[0,-1],[-1,0]]
if d > h:
    d=h
# if h == 1:
# elif h==2:
# for ct in range(d):
#     mirutoko = seen[ct]
#     for iti in mirutoko:
#         # print(men[iti[0]][iti[1]])
#         for i in idou:
#             gyou=iti[0]
#             retu=iti[1]
#             if iti[0]+i[0] < h and iti[1]+i[1] < w and -1 < iti[0]+i[0] and -1 < iti[1]+i[1]:
#                 if men[gyou+i[0]][retu+i[1]] != '#':# and ct < men[iti[0+i[0]]][iti[1+i[1]]]:
#                     print('Yes0')
#                     print(gyou+i[0],retu+i[1],[h,w],[i])
#                     if men[gyou+i[0]][retu+i[1]] == '.':
#                         men[gyou+i[0]][retu+i[1]] = (ct+1)
#                         #seen[0].append([gyou,retu])
#                         print('Yes1')
#                     elif ct+1 < men[gyou+i[0]][retu+i[1]]:
#                         men[gyou+i[0]][retu+i[1]] = (ct+1)
#                         #seen[0].append([gyou,retu])
#                         print('Yes2')
#                     else:
#                         print('No2')
#                     seen[ct+1].append([gyou+i[0],retu+i[1]])
                    
#                 else:
#                     print('No1')
#             else:
#                 print('No0')
#                 print(iti[0]+i[0],iti[1]+i[1],[h,w])

# ans=0
# for gyou in men:
#     for i in gyou:
#         if i != '#' and i != '.':
#             ans+=1
# print(ans)


# uu=0
# for u in men:
#     uu=''.join([str(x) for x in u])
#     print(uu)
# #print(seen)
# # for ct in range(d):
# #     for hi in h:
# #         for a in men[hi]:
# #             if a == 'H':
# #                 seen.append([hi,a])
# #                 for _ in range()


# 40