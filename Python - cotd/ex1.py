def newstring(str):

    words = [word for word in str.split()]
    # Create dict using 'words' item as keys. 
    # This will remove any duplicates due.
    # dictionary is then converted back into a list

    mylist = list(dict.fromkeys(words))

    mynewlist = ' '.join(sorted(mylist)) # returns a sorted list made out of the characters of the string

    return mynewlist
    
print(newstring('hello world and practice makes perfect and hello world again'))