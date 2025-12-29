from functools import reduce

INPUT_FNAME = "day6.input"

ans = 0
add = lambda x, y: x + y
mul = lambda x, y: x * y
lines = []

with open(INPUT_FNAME) as file:
    # load and split last line of file to retrieve columnar operators
    # read line by line (doesn't even have to be sequential reads)
    # reduce each term using operators retrieved during the first step
    # dunno how python handles file reads but in theory this only requires
    # at most 3 lines to be held in memory
    # read:
    # https://stackoverflow.com/questions/46258499/how-to-read-the-last-line-of-a-file-in-python
    # https://docs.python.org/3/tutorial/inputoutput.html (f.seek())
    # naive version first
    for line in file:
        lines.append(list(line.rstrip().split()))
    m, n = len(lines), len(lines[0])
    for i in range(n):
        op = add if lines[-1][i] == '+' else mul
        temp = reduce(op, [int(lines[j][i]) for j in range(m-1)])
        ans += temp

print(f"The sum of answers is {ans}.")

