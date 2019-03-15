#encoding = utf8
#password guest

print('猜密碼遊戲')
pw = input('請輸入密碼: ')
test = 0
chance = 2

while pw != '123456':
    if test < 2:
        print('密碼錯誤! 還有%d次機會' %chance)
        pw = input('請輸入密碼: ')
        test += 1
        chance -= 1        
    else:
        print('遊戲失敗')
        break
else:
    print('答對了!!')