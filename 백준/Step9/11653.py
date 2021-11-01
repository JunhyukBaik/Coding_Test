n = int(input())
bh = 2
while True:
  for i in range(2, n+1):
    if n % i == 0:
      print(i)
      n = n // i
      break
  if n < 2:
    break
