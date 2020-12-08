def up_low(s):
    a = {"upper":0, "lower":0}
    
    
    for char in s:
        if char.isupper():     # isupper checks for every upper case letter
            a["upper"] += 1
        elif char.islower():   # islower check for every lower case letter
            a["lower"] += 1
                     
    print("Upper -> ", a["upper"])
    print("lower -> ", a["lower"])

print(up_low("Hello world"))