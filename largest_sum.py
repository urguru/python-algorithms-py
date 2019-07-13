import sys
def largest_sum_calc(arr):
    if len(arr)==0:
        return "Input size is zero"
        
    largest_sum=arr[0]
    largest_so_far=arr[0]
    for i in range(1,len(arr)):
        largest_so_far=max(arr[i],largest_so_far+arr[i])
        largest_sum=max(largest_so_far,largest_sum)

    return largest_sum

print(largest_sum_calc([-1,-2,-3,4,5,7,112,23,-112,87,12,-43,65,-23]))
