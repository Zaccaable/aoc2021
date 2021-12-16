with open('day1_input.txt', 'r') as f:
    beeps = [int(line.replace('\n', '')) for line in f.readlines()]

count_part1 = 0
for i, beep in enumerate(beeps):
    if i > 0 and beeps[i] > beeps[i-1]:
        count_part1 += 1

print(f'The answer to part 1 is: {count_part1}')

count_part2 = 0
for i, beep in enumerate(beeps):
    if i > 0 and beeps[i] + beeps[i - 1] + beeps[i - 2] > beeps[i-1] + beeps[i - 2] + beeps[i - 3]:
        count_part2 += 1

print(f'The answer to part 2 is: {count_part2}')