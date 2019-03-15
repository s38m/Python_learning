#encoding = utf8
#password guest

print('猜密碼遊戲')
pwd = '123456'
chance = 3

while chance > 0:
    data = input('請輸入密碼: ')
    if pwd == data:
        print('恭喜你!猜對了!')
        break
    else:
        chance -= 1
        print('密碼錯誤! 剩餘%d次機會' %chance)
else:
    print('遊戲失敗!!')