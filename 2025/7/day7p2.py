# could naively backtrack
# if there are no splitters below particle's current position, backtrack to previous splitter
# 

INPUT_FNAME = "day7.input"

ans = 0

with open(INPUT_FNAME) as manifold:
    beams = set()
    for line in manifold:
        line = line.rstrip()
        for i, c in enumerate(line):
            match c:
                case 'S':
                    beams.add(i)
                case '^':
                    if i in beams:
                        ans += 1
                        beams.remove(i)
                    if i > 0:
                        beams.add(i-1)
                    if i < len(line) - 1:
                        beams.add(i+1)
                case _:
                    pass

print(f'The beam was split {ans} times.')

