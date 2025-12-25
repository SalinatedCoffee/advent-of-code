def isSilly2(num: str) -> bool:
    if len(num) % 2:
        return False
    for i in range(len(num) // 2):
        if num[i] != num[i + len(num) // 2]:
            return False

    return True

# how to traverse id range?
# brute force?
# 'just make it exist first; you can make it better later'
"""
with open("single_tests.input") as tests:
    for test in tests:
        test = test.rstrip()
        print(f"{test} is{' ' if isSilly(test) else " not "}silly.")
"""
# sliding window?
# how to decide when to extend window?
# brute force...?
# I swear I've solved this problem on leetcode before (or similar)
# 

ans = 0

with open("day2.input") as id_ranges:
    for id_range in id_ranges.readline().split(','):
        s, e = id_range.split('-')
        for i in range(int(s), int(e)+1):
            ans += i if isSilly(str(i)) else 0

print(f"The sum is {ans}.")

