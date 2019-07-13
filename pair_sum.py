def pair_sum(arr,k):
    if len(arr)<2:
        print('Array is too small')
        return
    seen=set()
    output=set()

    for num in arr:
        target=k-num
        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num,target),max(num,target)))

    for a,b in output:
        print(a,b)

pair_sum([1,2,3,4,2,2],4)