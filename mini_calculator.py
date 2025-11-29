a=int (input("Enter the value of A:"))
b=int (input("Enter the value of B:"))
operation=input("Enter the operation : add/sub/multiply/divide : ")
if a >= 0 and b >=0:
    if(operation=="add"):
        print(a+b)
    elif(operation=="sub"):
        print(a-b)
    elif(operation=="multiply"):
        print(a*b)
    elif(operation=="divide"):
        if b==0:
            print("cannot divided by zero")
        else:
            print(a/b)
    else:
       print("invalid operation")
else:
    print("Please only enter positive number ")