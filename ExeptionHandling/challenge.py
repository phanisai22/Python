x = int(input("enter the first number : "))
y = int(input("enter the second number : "))
try:
    z = x / y
    print(z)
except (ZeroDivisionError, TypeError):
    print("cannot handle the arithmetic .")
