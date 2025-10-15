def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])
    
    if arr==[]:
        arr.append([n, 1])
    print(arr)
    return arr
# factorization(24) 
factorization(20596743834967217731323525323803952313616238702337354308363233353310617617650545138317671939264209492298243621150709975444649092424695197963762450352178818
) 
## [[2, 3], [3, 1]] 
##  24 = 2^3 * 3^1
