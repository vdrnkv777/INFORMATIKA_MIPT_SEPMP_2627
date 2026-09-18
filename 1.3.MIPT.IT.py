a = input()
m = []

while a != 'end':
    m.append(int(a))
    a = input()

x = int(input())  

if x in m:
    print("Номер: ", m.index(x))
else:
    print("нема сорри")