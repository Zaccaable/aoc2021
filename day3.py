with open('day3_input.txt', 'r') as f:
    values = [line.replace('\n', '') for line in f.readlines()]

binary_length = len(values[0])
gamma = ''
epsilon = ''

for i in range(binary_length):
    if sum([int(value[i]) for value in values]) / len(values) > 0.5:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

gamma_dec = int(gamma, 2)
epsilon_dec = int(epsilon, 2)

print(f'Gamma: {gamma} is {gamma_dec} in decimal, epsilon {epsilon} is {epsilon_dec} in decimal. Power consumption is {gamma_dec * epsilon_dec}')