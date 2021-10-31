N = int(input())
count = 1
cnt = 1
cnt_six = 6

while N > cnt:
    count += 1
    cnt += cnt_six
    cnt_six += 6
    
print(count)