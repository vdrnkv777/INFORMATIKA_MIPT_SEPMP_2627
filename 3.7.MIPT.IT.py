file_in = open('input.txt', 'r')
numbers = file_in.read().split()
file_in.close()

max_count = 0
best_number = numbers[0]

for i in range(len(numbers)):
    count = 0
    for j in range(len(numbers)):
        if numbers[i] == numbers[j]:
            count += 1
    if count > max_count:
        max_count = count
        best_number = numbers[i]

file_out = open('output.txt', 'w')
file_out.write(best_number)
file_out.close()
