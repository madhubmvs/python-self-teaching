weight = float(input('Enter weight: '))
unit_measure = input("Kg(k) or Lb(l) : ")

if unit_measure.upper() == "L":
    print("The weight in Kg is: " +str(round(weight * 0.454, 2)))
elif unit_measure.upper() == "K":
    print("The weight in lbs is: " +str(round(weight/0.454, 2)))
else:
    print('Invalid input')
