def array_rotation(arr1,arr2):
    len1=len(arr1)
    len2=len(arr2)
    if len1!=len2:
        return False
    i=0
    for i in range(len1):
        if arr1[i]==arr2[0]:
            for j in range(len2):
                if arr1[i%len1]!=arr2[j]:
                    return False
            return True
    
    return False

print(array_rotation([1,2,3],[1,2,3,4]))