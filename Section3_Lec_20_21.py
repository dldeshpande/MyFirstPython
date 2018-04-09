

def sprint(name= "I",age =30):
    print("My name is ", name,"My age is ", age)


sprint("you",27)

# used infinite argument

def print_king(*solder):
    for person in solder:

        print("This is :", person)

print_king("joe","mark","henry","raw")

# return values from function

def print_add(num1,num2):
    return  num1 + num2

math1=print_add(10,20)
math2=print_add(54,50)
print("The addition of 1st number is : ", math1, "The addition of 2nd number is : ", math2)


