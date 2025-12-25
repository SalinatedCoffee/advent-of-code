def bankJoltage(bank: str) -> int:
    ret = 0
    for i in range(len(bank)):
        for j in range(i+1, len(bank)):
            ret = max(ret, int(bank[i] + bank[j]))
    return ret

INPUT_FNAME = "day3.input"

ans = 0

with open(INPUT_FNAME) as banks:
    for bank in banks:
        bank = bank.rstrip()
        ans += bankJoltage(bank)

print(f"Total output joltage: {ans}")

