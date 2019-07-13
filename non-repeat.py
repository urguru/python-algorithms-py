def non_repeating(str):
    count={}

    for i in str:
        count[i]=count.get(i,0)+1
    
    for i in count:
        if count[i]==1:
            return i
        
    return None

print(non_repeating('abcdefghabcdefghi'))