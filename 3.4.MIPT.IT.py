numbers = open('input.txt').read().split()
for i in range(0, len(numbers) - 1, 2): numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
open('output.txt', 'w').write(' '.join(numbers))
