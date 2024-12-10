#bruteforce

# arr=[4,5,0,2,0,1]

# count=0
# while 0 in arr:
#     arr.remove(0)
#     count+=1

# for i in range(count):
#     arr.append(0)
# print(arr)

#remove val   #pop index   #append val
#another approach                                           

# length = len(arr)

# for index in range(0,length):
#     value=arr[index]
#     if value ==0:
#         arr.append(value)
#         arr.remove(value)
# return arr


#another fucking approach
arr = list(map(int, input().split()))

zero = arr.count(0)
arr = [x for x in arr if x != 0]

arr.extend([0] * zero)

print(arr)
