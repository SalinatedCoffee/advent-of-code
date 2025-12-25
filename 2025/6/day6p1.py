INPUT_FNAME = "test.input"

ans = 0

with open(INPUT_FNAME) as file:
    # load and split last line of file to retrieve columnar operators
    # read line by line (doesn't even have to be sequential reads)
    # reduce each term using operators retrieved during the first step
    # dunno how python handles file reads but in theory this only requires
    # at most 3 lines to be held in memory
    # read:
    # https://stackoverflow.com/questions/46258499/how-to-read-the-last-line-of-a-file-in-python
    # https://docs.python.org/3/tutorial/inputoutput.html (f.seek())
    break

print(f"The sum of answers is {ans}.")

