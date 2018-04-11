import re

previous = 0
run = True
print("our magical calculator")

def perforMath():
   global run
   global previous
   equation = ""

   if previous == 0:
       equation = input("Enter equation ")
   else:
       equation = input(str(previous))

   if equation == 'quit':
       print("good by human")
       run = False
   else:
       equation = re.sub('[A-za-z,:'""']','', equation)
   if previous == 0:
       previous = eval(equation)
   else:
       previous = eval(str(previous) +equation)

while run:
    perforMath()

