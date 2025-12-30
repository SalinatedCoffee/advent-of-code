# two-row simulation?
# starting at the first row and moving downwards
# one row tracks position of beams at previous step of time
# another tracks position of current
# once current beam positions have been determined, swap them and overwrite oldest in the next step
# or better yet, just keep track of the columns that currently have a beam traveling through them
# a set should work
# then for each row, scan through for splitters and check the set for a beam
# update accordingly
# ???
# profit

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

