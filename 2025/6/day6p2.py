from functools import reduce

INPUT_FNAME = "day6.input"

ans = 0
add = lambda x, y: x + y
mul = lambda x, y: x * y
lines = []

def ident_col(ln: str, s: int) -> int:
    while ln[s] == ' ':
        s -= 1
    return s

with open(INPUT_FNAME) as file:
    # can't use split since we need to conserve whitespaces
    # use last row to determine 'width' of each column
    # can probably use reduce() to generate each columnar digit
    for line in file:
        lines.append(line.rstrip('\n'))
    m, n = len(lines), len(lines[0])
    i = n-1
    while i >= 0:
        s = ident_col(lines[-1], i)
        # there's gotta be a better way of doing this
        op = add if lines[-1][s] == '+' else mul
        res = 0 if lines[-1][s] == '+' else 1
        for j in range(i, s-1, -1):
            num_str = reduce(lambda x, y: x + y, [lines[k][j] for k in range(m-1)]).strip()
            #print(f'{(num_str)}')
            res = op(res, int(num_str))
        ans += res
        #print(res)
        i = s - 2


print(f"The sum of answers is {ans}.")

