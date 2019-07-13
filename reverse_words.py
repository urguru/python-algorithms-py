def reverse_words(str):
    words = str.strip().split()
    words.reverse()
    revstr = ""
    for word in words:
        revstr += word+" "
    revstr.rstrip()

    return revstr


print(reverse_words('Hello Everyone My Name is Guruprasad'))


def reverse_words2(str):
    return ' '.join(reversed(str.split()))


print(reverse_words2('Hello Everyone My Name is Guruprasad'))


def reverse_words3(str):
    return ' '.join((str.split())[::-1])


print(reverse_words3('Hello Everyone My Name is Guruprasad'))


def reverse_words4(str):

    length = len(str)
    spaces = [' ']
    words = list()
    i = 0
    while i < length:
        if str[i] not in spaces:
            word_start = i

            while i < length and str[i] not in spaces:
                i += 1

            words.append(str[word_start:i])
        i += 1

    return ' '.join(reversed(words))


print(reverse_words4('Hello Everyone My Name is Guruprasad'))
