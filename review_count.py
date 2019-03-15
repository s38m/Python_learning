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