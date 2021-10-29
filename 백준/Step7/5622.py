phone = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
sum = 0
num = input()
for i in range(len(num)):
    for j in range(len(phone)):
        if num[i] in phone[j]:
            sum = sum + j + 2
print(sum+len(num))