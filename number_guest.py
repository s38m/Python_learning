#encoding = utf-8
#Number guest

import random
print('猜數字遊戲開始囉~')
start = int(input('請決定本局最小的數字: '))
end = int(input('請請決定本局最大的數字: '))

r = random.randint(start, end)
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