def add_calc(num1, num2):
    answer = num1 + num2

    return answer

added_number = add_calc(5,5)

print(added_number + 20)


def grade(name, h, a, f):

    overall = (((h/25) + (a/50) + (f/100))/3) * 100

    return f"{name} : final IT grade -> {overall}"




print(grade('Harry', 12, 25, 50))