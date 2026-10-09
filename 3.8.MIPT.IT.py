file_in = open('input.txt', 'r')
lines = file_in.read().split('\n')
file_in.close()
N = int(lines[0])                
numbers = lines[1].split()     
middle_index = (N - 1) // 2     
median = numbers[0]              
for i in range(len(numbers)):
    count_less = 0            
    for j in range(len(numbers)):
        if numbers[j] < numbers[i]:
            count_less += 1
    if count_less == middle_index:
        median = numbers[i]
        break       
file_out = open('output.txt', 'w')
file_out.write(median)
file_out.close()
