# patterns = [format(i, '06b') for i in range(64)]
# print(patterns)
# patterns=["000000","000001","000010","000011","000100","000101","000110","000111"]
# ===================================================================================================
# patterns = [[(i >> bit) & 1 for bit in reversed(range(6))] for i in range(64)]

# nedan = [120, 170, 40, 200, 350, 80]
# ans = []
# ans1=[]
# aaa=[0]
# for u in patterns:
#     ct = -1
#     an = 0
#     for i in u:
#         ct += 1
#         if i == 1:       # ← 文字として比較
#             an += nedan[ct]
#     ans.append([an,u])    # elseを外に出す
#     if aaa[-1] < an and an <= 500:
#         aaa.append(an)
# ans_srt = sorted(ans, key=lambda x: x[0])
# for i in ans_srt:
#     print(i)
# print(aaa)
# print(sum(aaa))


# # patterns = [format(i, '06b') for i in range(64)]
# # print(patterns)
# # patterns=["000000","000001","000010","000011","000100","000101","000110","000111"]
# patterns = [[(i >> bit) & 1 for bit in reversed(range(6))] for i in range(64)]

# nedan = [120, 170, 40, 200, 350, 80]
# ans = 0

# for u in patterns:
#     ct = -1
#     an = 0
#     for i in u:
#         ct += 1
#         if i == 1:       # ← 文字として比較
#             an += nedan[ct]
#     if ans < an:
#         # ans.append([an,u])    # elseを外に出す
#         ans = an
# # ans_srt = sorted(ans, key=lambda x: x[0])
# # for i in ans_srt:
# #     print(i)
# print(ans)


# ===============================================================================================

patterns = [[(i >> bit) & 1 for bit in reversed(range(6))] for i in range(64)]
nedan = [120, 170, 40, 200, 350, 80]
ans = []
aaa=[0]
for u in patterns:
    ct = -1
    an = 0
    for i in u:
        ct += 1
        if i == 1:
            an += nedan[ct]
    ans.append([an,u])
    if aaa[-1] < an and an <= 500:
        aaa.append(an)
print(aaa)
print(sum(aaa))

# print('777777')
# print(2**10)
# print(2**100)
# print(100*101/2)