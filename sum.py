def sum1(n):
    final_sum=0
    for i in range(n+1):
        final_sum+=i
    
    return final_sum

print(sum1(10))

def sum2(n):
    return n*(n+1)/2

print(sum2(10))