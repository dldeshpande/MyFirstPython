import  random

class enemy:
    def __init__(self,attackl,attackh):
        self.attackl = attackl
        self.attackh = attackh

    def get_attack(self):
        print(self.attackh)

enemy1 = enemy(20,89)
enemy1.get_attack()

enemy2 = enemy(90,99)
enemy2.get_attack()

#
# hpplayer = 260
# enemyatkl = 60
# enemyatkh = 80
#
#
# while hpplayer > 0:
#     dmg = random.randrange(enemyatkl, enemyatkh)
#     hpplayer = hpplayer - dmg
#     print("Your strike rate is : ", dmg, "Your damage point. current HP point is", hpplayer)
#     break
#     if hpplayer <= 30:
#         hpplayer = 30
#         print("Your helth is too low contact to nearest helth port")
#         continue
#     if hpplayer == 0:
#         print("Your suppose to be die""You have to respwan to nearest hospital")
