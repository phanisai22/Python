t_bill = float(
    input("Welcome to the tip calculator\nWhat was the total bill? $"))
t_people = int(input("How many people to split the bill? "))
percentage = float(
    input("What percentage tip would you like to give? 10, 12, or 15? "))

t_amount = t_bill + (percentage/100) * t_bill
each_person = t_amount/t_people

print("Each person should pay: ${}".format(round(each_person, 2)))
