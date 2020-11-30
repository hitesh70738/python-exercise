m_mark = float(input('Enter Math mark -> '))
c_mark = float(input('Enter Chemistry mark -> '))
p_mark = float(input('Enyer Physics mark -> '))

Overall = (m_mark + c_mark + p_mark)/3
print(Overall)
if Overall < 40:
    print("You failed")
elif Overall >= 70:
    print("A")
elif Overall >= 60:
    print("B")
elif Overall >= 50:
    print("C")
elif Overall >= 40:
    print("D")
else:
    print("Error try again")

 