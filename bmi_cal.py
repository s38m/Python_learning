# coding = UTF-8
height = float(input('請輸入身高(CM): ')) / 100
weight = float(input('請輸入體重(KG): '))
bmi = weight / height**2

print('你的BMI為: ' , bmi)

if bmi >= 24:
    if bmi < 27:
        print('過重')
    elif bmi < 30:
        print('輕度肥胖')
    elif bmi < 35:
        print('中度肥胖')
    else:
        print('重度肥胖')
elif bmi >= 18.5:
    print('正常')
else:
    print('過輕')
