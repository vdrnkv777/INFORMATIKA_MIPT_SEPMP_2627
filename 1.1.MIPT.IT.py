p = input().split()

p[0] = int(p[0])
p[2] = int(p[2])

if p[1] == "+":
   print(p[0] + p[2])
elif p[1] == "-":
   print([p[0] - p[2]])
elif p[1] == "*":
   print(p[0]*p[2])
elif p[1] == "/":
   print(p[0]/p[2])