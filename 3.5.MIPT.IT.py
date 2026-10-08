numbers = open('input.txt').read().split()
open('output.txt', 'w').write(' '.join([numbers[-1]] + numbers[:-1]))
