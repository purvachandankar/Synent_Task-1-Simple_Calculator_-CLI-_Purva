a = float(input("Enter first no: "))
b = float(input("Enter second no:"))

class Calculator:
    def addition (self,a,b):
        return a+b
    
    def subtraction (self,a,b):
        return a-b
    
    def multiplication (self,a,b):
        return a*b
    
    def division (self,a,b):
        if b==0:
            return None
        else:
            return (a/b)
    
c1 = Calculator()

while True:
    print("\n1.Addition\n")
    print("2.Subtraction\n")
    print("3.Multiplication\n")
    print("4.Division\n")
    print("5.Exit\n")   
    choice = input("Enter your choice:")

    if choice == "1":
        print ("Addition = ",c1.addition(a, b))
    elif choice == "2":
        print ("Subtraction = ",c1.subtraction(a,b))
    elif choice == "3":
        print ("Multiplication = ",c1.multiplication(a,b))
    elif choice == "4":
        result = c1.division(a,b)
        if result is None:
            print("Division by zero is not allowed")
        else:
            print("Division = ",result)
    elif choice == "5":
        print("....Exit....")
        break
    else:
        print("In-valid choice")


