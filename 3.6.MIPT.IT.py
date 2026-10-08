file_in = open('input.txt', 'r')
numbers = file_in.read().split()
file_in.close()

file_out = open('output.txt', 'w')
for i in range(len(numbers)):
    count = 0
    for j in range(len(numbers)):
        if numbers[i] == numbers[j]:
            count += 1
    if count == 1:
        print(numbers[i], end=' ', file=file_out)
file_out.close()
