import pygame
def bullet_Hit_Player(predator,victim,bullets):
        #collision des bullets avec la victime
        hit_On_P1=pygame.sprite.spritecollide(victim,bullets,True)
        if hit_On_P1:
            predator.updateScore(500)
            print(predator.name+" : ",predator.score)
            print(victim.name+ " touché par un bullet")
            victim.decreaseHP(predator.Dmg)
            print(victim.HP)
            victim.respawn()