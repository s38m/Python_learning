def sum_of_list(params):
    total = 0
    for param in params:
        total += param
    return total

sum = []
times = 0
print('輸入 \'q\' 開始計算')

while True:
    times += 1
    num = input('請輸入第 %d 個數字: ' %times)
    if num != 'q':
        sum.append(float(num))
    else:
        break
print(sum_of_list(sum))