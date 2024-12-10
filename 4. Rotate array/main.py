
#left
# arr=[7, 3, 9, 1]
# d=int(input())

# #brute force

# for i in range(d):
#     arr.append(arr[0])
#     arr.pop(0)
# print(arr)

#best
arr = [7, 3, 9, 1]
d = 9
n = len(arr)
d = d % n  # 9 % 4 = 1

arr = arr[d:] + arr[:d]  
print(arr)

#right
arr[:]=arr[n-d:]+arr[:n-d]