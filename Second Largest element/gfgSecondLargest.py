#Description
# second largest element ko return karna hai 
# agar nhi hai to -1 return karna hai.


#approach 1

def unique(arr):
    uni=[]
    for i in arr:
        if i not in uni:
            uni.append(i)
    return uni

arr=list(map(int, input().split()))
arr.sort()
rtu=unique(arr)

try:
    return(rtu[-2])
except:
    return -1

#approach 2
arr=list(map(int,input().split()))
arr.sort()
narr=list(set(arr))
try:
    print(narr[-2])
except:
    print(-1)


