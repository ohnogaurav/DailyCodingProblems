#reversing an arry

#best

arr=[1,2,4,5,6,4]
# arr.reverse()
# return arr

#optimal two point
n=len(arr)
forward,backward=0,n-1
while forward<backward:
    arr[forward],arr[backward]=arr[backward],arr[forward]

    forward+=1
    backward-=1
print(arr)