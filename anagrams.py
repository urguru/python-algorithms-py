def anagrams(str1, str2):
    str1 = str1.replace(' ', '').lower()
    str2 = str2.replace(' ', '').lower()

    return sorted(str1) == sorted(str2)


print(anagrams('Guru', 'Santu'))


def anagrams2(str1, str2):
    str1 = str1.replace(' ', '').lower()
    str2 = str2.replace(' ', '').lower()

    if(len(str1)!=len(str2)):
        return False
    
    count={}

    for character in str1:
        count[character]=count.get(character,0)+1

    for character in str2:
        if character in count:
            count[character]-=1
        else:
            count[character]=1
        
    for value in count.values():
        if value!=0:
            return False
    
    return True

print(anagrams2('Letter','terlet'))