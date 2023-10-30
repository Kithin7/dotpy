print('\np20')
# Remove the K'th element from a list.
remove_at = [["a", "b", "c", "d"], 2]
print(remove_at)
remove_at[0].pop(remove_at[1]-1)
print(remove_at[0])

print('\np21')
# Insert an element at a given position into a list
insertat = ['alfa', ["a", "b", "c", "d"], 2]
print(insertat)
insertat[1].insert(insertat[2], insertat[0])
print(insertat[1])

print('\np22')
# Create a list containing all integers within a given range.
a, b = 4, 9
print(a, b)
lrange = []
if a < b:
    for i in range(a, b+1):
        lrange.append(i)
else:  # If first argument is smaller than second, produce a list in decreasing order.
    for i in range(a-b+1):
        lrange.append(a)
        a -= 1
print(lrange)

print('\np23')
# Extract a given number of random selected elements from a list.
# Hint: Use the built-in random number generator (and the result of problem P20.)????
import random as rnd
rng_select = [["a", "b", "c", "d", "e", "f", "g", "h"], 3]
rng_list = []
for nn in range(rng_select[1]):
    rng_list.append(rng_select[0][rnd.randint(0, len(rng_select[0])-1)])
print(rng_select)
print(rng_list)

print('\np24')
# Lotto: Draw N different random numbers from the set 1..M.
# Hint: Combine the solutions of problems P22 and P23.
lotto_sel = [6, 49]  # [N, M], N = number to output, M = 1-M range
lotto_nums = []
for lotto in range(lotto_sel[0]):
    lotto_nums.append(rnd.randint(1, lotto_sel[1]))
print(lotto_nums)

print('\np25')
# Generate a random permutation of the elements of a list.
# Hint: Use the solution of problem P23
perm = ["a", "b", "c", "d", "e", "f"]
rng_perm = []
for p in range(len(perm)):
    q = rnd.randint(0, len(perm)-1)
    rng_perm.append(perm[q])
    perm.pop(q)
    print(perm)
    print(rng_perm)

print('\np26')
# Generate the combinations of K distinct objects chosen from the N elements of a list
# In how many ways can a committee of 3 be chosen from a group of 12 people?
# We all know that there are C(12,3) = 220 possibilities (C(N,K) denotes the well-known binomial coefficients).
# For pure mathematicians, this result may be great. But we want to really generate all the possibilities in a list.
combo_list = ["a", "b", "c", "d", "e", "f"]
combos = []
# remember, order doesn't matter!


#def find_combos(list_, n, k):
    #for:


