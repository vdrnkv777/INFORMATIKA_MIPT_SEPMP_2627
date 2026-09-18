n = int(input()) 
a = []

for i in range(n):
    if i == 0 or i == 1:
        a.append(1)
    else:
        a.append(a[i-1] + a[i-2])

print(a)