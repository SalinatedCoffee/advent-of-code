LOCK_SIZE = 100
pos = 50
ans = 0

with open("day1.input") as instructions:
    for instruction in instructions:
        dir, dist = instruction[0], int(instruction[1:])
        match dir:
            case 'L':
                ans += ((LOCK_SIZE - pos) % LOCK_SIZE + dist) // LOCK_SIZE
                dist *= -1
            case 'R':
                ans += (pos + dist) // LOCK_SIZE
            case _:
                break
        pos = (pos + dist) % LOCK_SIZE

print(f'The (actual) passcode is {ans}.')

