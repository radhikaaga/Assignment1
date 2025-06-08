from itertools import groupby

# Read input string
s = input()

# Apply groupby and print the result as (count, character)
result = [(len(list(group)), int(key)) for key, group in groupby(s)]
print(*result)
