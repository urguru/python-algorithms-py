def most_frequent(arr):
    count={}
    max_count=0
    max_item=None

    for i in arr:
        count[i]=count.get(i,0)+1

        if count[i]>max_count:
            max_count=count[i]
            max_item=i
    
    for x,y in sorted(count.items()):
       print(x,y)

most_frequent([1,2,3,4,1,2,3,1,2,1])