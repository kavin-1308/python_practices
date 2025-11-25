num=int(input("Enter the number : "))
if num<0:
    print("Enter a valid number")
else:
    factorial=1
    for i in range(1,num+1):
        factorial*=i
print("Factorial of ",num,"is ",factorial)
