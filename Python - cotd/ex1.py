def newstring(str):

    words = [word for word in str.split()]

    mylist = list(dict.fromkeys(words))

    mynewlist = ' '.join(sorted(mylist))

    return mynewlist
    
print(newstring('hello world and practice makes perfect and hello world again'))