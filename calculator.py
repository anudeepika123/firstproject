def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
print("1.addition")
print("2.substraction")
print("3.multiplication")
print("4.division")
choice=int(input('enter the value'))
num1=int(input("enter a value"))
num2=int(input("enter b value"))
if choice==1:
        print("add",add(num1,num2))
elif choice==2:
        print("sub",sub(num1,num2))
elif choice==3:
        print("add",mul(num1,num2))
elif choice==4:
        print("add",div(num1,num2))
else:
        print("invalid")

    
    

