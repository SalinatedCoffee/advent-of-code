INPUT_FNAME = "day5.input"

ans = 0

# list of ranges, empty line, list of ids
# if given id is not in any range, it is rotten
# merge ranges
# if ranges can be sorted in order of starting id
# can use binary search to update
# also need to keep track of ending id
# ...or do we?
# since all ranges are merged
# if starting id i is largest id less than some id n
# any range with starting id less than i will never include n
# so the problem now becomes:
# how do we collate given ranges while maintaining their order (ascending by start id)
# 
ranges = []
ids = []

with open(INPUT_FNAME) as lines:
    tgt = ranges
    for line in lines:
        if line == "":
            break


print(f"{ans}.")

