# p10
# Run-length encoding of a list.
# from p09
dups = ("a", "a", "a", "a", "b", "c", "c", "a", "a", "d", "e", "e", "e", "e")
packed = [[""]]
for i in dups:
    if i == packed[-1][0]:  # if the same, then add to the sub list
        packed[-1].append(i)
    else:  # if not then same, then make a new sub list and add it
        packed.append(list(i))
packed.pop(0)

print('\np10')
packed_run = []
for j in range(len(packed)):
    packed_run.append([len(packed[j]), packed[j][0]])
print(packed_run)

print('\np11')
# Modified run-length encoding
packed_run_mod = []
for j in range(len(packed)):
    if len(packed[j]) == 1:
        packed_run_mod.append(packed[j][0])
    else:
        packed_run_mod.append([len(packed[j]), packed[j][0]])
print(packed_run_mod)

print('\np12')
# Decode a run-length encoded list
unpacked = []
for k in packed_run_mod:
    if len(k) > 1:
        for l in range(k[0]):
            unpacked.append(k[1])
    else:
        unpacked.append(k)
print(unpacked)

print('\np13')
# Run-length encoding of a list (direct solution)
direct_encode = []
count = 1
for p in range(len(dups)):
    if p == len(dups)-1:  # handle last check
        direct_encode.append([count, dups[p]])
    elif p < len(dups)-1 and dups[p] == dups[p+1]:  # match; keep counting
        count += 1
    else:  # no match; append & reset
        if count == 1:
            direct_encode.append([dups[p]])
        else:
            direct_encode.append([count, dups[p]])
        count = 1
        print(direct_encode)
print(direct_encode)

print('\np14')
# Duplicate the elements of a list.
duppy = ("a", "b", "c", "c", "d")
duplicated = []
for p in duppy:
    duplicated.append(p)
    duplicated.append(p)
print(duppy)
print(duplicated)

print('\np15')
# Replicate the elements of a list a given number of times.
repli = [["a", "b", "c"], 3]
replicated = []
for m in repli[0]:
    for n in range(repli[1]):
        replicated.append(m)
print(repli)
print(replicated)

print('\np16')
# Drop every N'th element from a list
drop = [("a", "b", "c", "d", "e", "f", "g", "h", "i", "k"), 3]
dropped = []
for d in range(len(drop[0])):
    if (d+1) % drop[1] != 0:
        dropped.append(drop[0][d])
        print(dropped)
print(drop)
print(dropped)

print('\np17')
# Split a list into two parts; the length of the first part is given
split = (("a", "b", "c", "d", "e", "f", "g", "h", "i", "k"), 3)
split_list = [split[0][0:split[1]], split[0][split[1]:-1]]
print(split)
print(split_list)

print('\np18')
# Given two indicies, I & K, slice the list containing the elements between I'th & K'th elements (inclusive), I-K.
chunk = (("a", "b", "c", "d", "e", "f", "g", "h", "i", "k"), 3, 7)
chunked_list = [chunk[0][chunk[1]-1:chunk[2]]]
print(chunk)
print(chunked_list)

print('\np19')
# Rotate a list N places to the left
rotate = [["a", "b", "c", "d", "e", "f", "g", "h"], -2]
rotated = []
for r in range(len(rotate[0])):
    rotated.append(rotate[0][r+rotate[1]])
print(rotate)
print(rotated)
# alternatively
rotate_alt = [["a", "b", "c", "d", "e", "f", "g", "h"], -2]
for rr in range(len(rotate_alt[0])+rotate_alt[1]):
    rotate_alt[0].append(rotate_alt[0][0])
    rotate_alt[0].pop(0)
print(rotate_alt)


