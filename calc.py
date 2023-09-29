def my_func(operation,n1,n2):
    if operation=="+":
        print("The Result is: " + str(n1+n2))
    elif operation=="-":
        print("The Result is: " + str(n1-n2))
    elif operation=="/":
        print("The Result is: " + str(n1/n2))
    elif operation=="x":
        print("The Result is: " + str(n1*n2))
    elif operation=="%":
        print("The Result is: " + str(n1%n2))  
    elif operation=="^":
        print("The Result is: " + str(n1**n2))
    else:
        print("Wrong Choice")
while 1:
    print("********* SIMPLE CALCULATOR *********")
    print("Enter The First Number: ")
    Num1=int(input())
    print("Enter The Second Number: ")
    Num2=int(input())
    print("+ For Addition\n- For Subscription\n/ For Division\nx For Multiplication\n% For Modules\n^ For Power")
    print("Enter Required Operation: ")
    strt=str(input())
    my_func(strt,Num1,Num2)
    