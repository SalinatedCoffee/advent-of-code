LOCK_SIZE = 100
pos = 50
ans = 0

with open("day1.input") as instructions:
    for instruction in instructions:
        dir, dist = instruction[0], int(instruction[1:])
        match dir:
            case 'L':
                pos -= dist
            case 'R':
                pos += dist
            case _:
                break
        pos %= LOCK_SIZE
        if pos == 0:
            ans += 1

print(f'The passcode is {ans}.')

