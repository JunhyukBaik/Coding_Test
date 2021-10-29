ca = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
sen = input()
for rp in ca:
    sen = sen.replace(rp, '#')
print(len(sen))