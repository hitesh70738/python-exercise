def up_low(s):
    a = {"upper":0, "lower":0}
    
    
    for char in s:
        if char.isupper():
            a["upper"] += 1
        elif char.islower():
            a["lower"] += 1
        else:
            pass

    
    print("Upper: ", a["upper"])
    print("lower: ", a["lower"])

print(up_low("Hello world"))