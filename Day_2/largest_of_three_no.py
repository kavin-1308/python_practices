def largest_of_three(a,b,c):
    if(a>=b and a>=c):
        return a
    elif(b>=a and b>=c):
        return b
    else:
        return c
    
x=float(input("Enter your first num : "))
y=float(input("Enter your second num : "))
z=float(input("Enter your third num : "))

print("The greatest num is :",largest_of_three(x,y,z) )