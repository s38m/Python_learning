#encoding = utf-8
#Number guest

import random

r = random.randint(1, 100)
chance = 10

while chance > 0:
    guest = int(input('猜猜數字是多少: '))
    chance -= 1
    if guest == r:
        print('恭喜你!猜對了!')
        break
    else:
        if chance > 0 and guest > r:
            print('太大囉~~ 還剩%d次機會' %chance)
        elif chance > 0 and guest < r:
            print('太小囉~~ 還剩%d次機會' %chance)
        else:
            print('沒機會了，GAME OVER~~')