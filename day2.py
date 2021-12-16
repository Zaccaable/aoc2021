with open('day2_input.txt', 'r') as f:
    instructions = [line.replace('\n', '') for line in f.readlines()]

x_part1 = 0
y_part1 = 0
for instruction in instructions:
    direction, amount = instruction.split()
    if direction == 'forward':
        x_part1 += int(amount)
    elif direction == 'up':
        y_part1 -= int(amount)
    elif direction == 'down':
        y_part1 += int(amount)

print(f'Part 1: Horizontal position is {x_part1}, vertical posistion is {y_part1} and the product is {x_part1 * y_part1}')

x_part2 = 0
y_part2 = 0
aim = 0

for instruction in instructions:
    direction, amount = instruction.split()
    if direction == 'forward':
        x_part2 += int(amount)
        y_part2 += aim * int(amount)
    elif direction == 'up':
        aim -= int(amount)
    elif direction == 'down':
        aim += int(amount)

print(f'Part 2: Horizontal position is {x_part2}, vertical posistion is {y_part2} and the product is {x_part2 * y_part2}')