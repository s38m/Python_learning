#encoding = utf-8
#file i/o exercise

data = []

with open('review.txt', 'r') as f:
    for line in f:
        data.append(line)
print('檔案讀取完成，總共有', len(data), '筆資料')

#average length for each data
sum_len = 0
for d in data:
    sum_len += len(d)
    avg = sum_len / len(data)
print('留言平均長度為', avg)

#sort: data shorter than 100
new = []
for d in data:
    if len(d) <100:
        new.append(d)
print('一共有', len(new), '筆留言長度小於100')

#sort: data include 'good'
good = []
for d in data:
    if 'good' in d:
        good.append(good)
print('一共有', len(good), '筆留言提到\'good\'')

#list comprehension
great = [d for d in data if 'great' in d]
# output = [運算結果 for var. in list 篩選條件]
print('一共有', len(good), '筆留言提到\'great\'')