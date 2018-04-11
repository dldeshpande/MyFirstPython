import random

playerhp  = 360
attackhpl = 60
attackhp  = 80

while playerhp > 0:
      dmg = random.randrange(attackhpl, attackhp)
      playerhp = playerhp - dmg

      if playerhp <= 30 :
         playerhp = 30

      print("Enenmy strike for: ", dmg ,"Damage point. current hp", playerhp)
      if playerhp == 0:
         print("You are suppose to be die")
      if playerhp ==30:
         print("yor helth range is low:")
         break