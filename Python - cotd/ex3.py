def zip(str1, str2):
    
    output =" "

    for i in range(len(str1)):
        output += str1[i] + str2[i]

    return output


print(zip("String","Fridge"))
print(zip("return","letter"))