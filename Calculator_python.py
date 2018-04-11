
# Addition function
def add(x, y):
    return x+y
#Subtraction function

def sub(x, y):
    return x-y

# Multiplication function
def mul(x, y):
    return x*y

#Division function

def div(x, y):
    return x/y

print("Select operation.")
print("1.Addition")
print("2.subtraction")
print("3.multiplication")
print("4.Division")

choice = input("Enter choice(1/2/3/4):")

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

if choice =='1':
         print(num1, "+", num2,"=", add(num1,num2))
elif choice =='2':
         print(num1, "-",num2, "=", sub(num1, num2))
elif choice =='3':
         print(num1, "*",num2, "=", mul(num1, num2))
elif choice == '4':
         print(num1, "/",num2,"=", div(num1,num2))
else:
         print("invalid operation")