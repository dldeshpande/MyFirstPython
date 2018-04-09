

def sprint(name= "I",age =30):
    print("My name is ", name,"My age is ", age)


sprint("you",27)

# used infinite argument

def print_king(*solder):
    for person in solder:

        print("This is :", person)

print_king("joe","mark","henry","raw")