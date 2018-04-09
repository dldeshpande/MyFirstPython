check = "hamburger"

if check == False:
   print("It is false")
elif check == "hamburger":
   print("hoo","It is yummy")
else:
   print("It is actual equal to True")

# using For loop

numbers = [12,13,14,15,16]
for item in numbers:
    print("The number is ", item)
# while loop
run = True
current = 1

while run:
    if current == 100:
        run = False
    else:
        print(current)
        current += 1