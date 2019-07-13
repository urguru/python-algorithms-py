def common_values(arr1,arr2):
    p1=0
    p2=0
    result=[]
    while p1<len(arr1) and p2<len(arr2):
        if arr1[p1]==arr2[p2]:
            result.append(arr1[p1])
            p1+=1
            p2+=1
        elif arr1[p1]>arr2[p2]:
            p2+=1
        else:
            p1+=1

    return result

print(common_values([1,2,4,6,8],[1,3,5,7,9]))

