n = int(input())
numbers = list()
for i in range(n):
    number = int(input())
    numbers.append(number)

for i in range(len(numbers)-1):
    least = i
    for j in range(i+1, len(numbers)):
        if numbers[j] < numbers[least]:
            least = j
    numbers[i], numbers[least] = numbers[least], numbers[i]
    
for i in numbers:
    print(i)