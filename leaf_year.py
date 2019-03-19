def is_leaf(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0 and year % 3200 != 0):
        return '潤年'
    else:
        return '平年'

y = int(input('請輸入年份: '))
print(is_leaf(y))