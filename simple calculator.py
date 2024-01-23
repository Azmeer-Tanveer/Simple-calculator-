print("===SIMPLE CALCULATOR===")

print("SELECT OPERATION: ")    
print("1:Addition")
print("2:Subtraction")
print("3:Multiplication")
print("4:Division")
print("5:Exit")

while True:

    choice=int(input("Select any 1 option:"))

    if choice== 5:
        print("Exiting calculator...")
        break


    num1=float(input("Enter first number= "))
    num2=float(input("Enter second number= "))
    
    result = None

    if choice== 1:
        result = num1+num2
        operation= "+"
    elif choice== 2:
        result = num1-num2
        operation= "-"    
    elif choice== 3:
        result = num1*num2
        operation= "*"
    elif choice== 4:    
        result = num1/num2
        operation= "/"
    else:
        print("invalid input")

    if result is not None:
        print(f"{num1} {operation} {num2} = {result}")
