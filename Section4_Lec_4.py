import  random

class enemy:
    attackl = 60
    attackh= 80

    def get_attack(self):
        print(self.attackl)

enemy1 = enemy()
enemy1.get_attack()

enemy2 = enemy()
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
