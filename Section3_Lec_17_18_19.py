

def my_first_function():
    print("Function in python")
    print("how to call function" + " in python")


my_first_function()

# passing argument in function


def my_first_function(fun1, fun2):
    print(fun1)
    print(fun2)


my_first_function("first argument", "second argument")
my_first_function("third argument", "fourth argument")

# passing argument while calling function
def details(name,age,address):
    print("My Name is: " + name,  "My age is: " + str(age), "My Address is : " + address)


details("George",27,"Boston")

# using the comma separator instead of concatenation
def details(name,age,address):
    print("My Name is:",  name, "My age is: ", age, "My Address is : ", address)


details("George",27,"Boston")


# value assignment in function

def details(name = "DD",age=32,address="INDIA"):
    print("My Name is: ", name, "My age is: ", age, "My Address is : ", address)


details()