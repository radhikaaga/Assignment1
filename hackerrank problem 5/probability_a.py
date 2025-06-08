from math import comb

# Read inputs
n = int(input())
letters = input().split()
k = int(input())

# Count how many 'a's are in the list
count_a = letters.count('a')

# If no 'a' or k is 0, probability is 0
if count_a == 0 or k == 0:
    print("0.000")
else:
    # Total ways to choose k indices from n
    total = comb(n, k)
    
    # Ways to choose k indices without any 'a' (i.e. all from n - count_a)
    without_a = comb(n - count_a, k) if n - count_a >= k else 0
    
    # Probability at least one 'a' is selected = 1 - P(no 'a')
    probability = 1 - (without_a / total)
    
    # Print result rounded to 3 decimal places
    print(f"{probability:.3f}")
