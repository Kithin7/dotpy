import numpy as np

# https://www.ic.unicamp.br/~meidanis/courses/mc336/problemas-lisp/L-99_Ninety-Nine_Lisp_Problems.html
print('\np01')
# Find the last box of a list.
my_list = [1,2,3,4,5,0]

print("last item = ", my_list[-1])

print('\np02')
# Find the last but one box of a list.
print("last item + 1 =", my_list[-2], my_list[-1])

print('\np03')
# Find the k'th element of a list.
k = 2
#k = int(input("index to find:  ")
print(f'index [{k}] = {my_list[k]}')

print('\np04')
# Find the number of elements of a list.
print(len(my_list))

print('\np05')
# Reverse a list.
my_list_r = []
for i in range(len(my_list)):
    my_list_r.append(my_list[len(my_list)-1-i])
print(my_list)
print(my_list_r)

print('\np06')
# Find out whether a list is a palindrome.
another_list = [1,2,3,2,1]
flag = False
flag2 = False
for i in range(int(np.floor(len(my_list)/2))):
    if my_list[i] == my_list[len(my_list)-1-i]:
        flag = True
    else:
        flag = False
for j in range(int(np.floor(len(another_list)/2))):
    if another_list[j] == another_list[len(another_list)-1-j]:
        flag2 = True
    else:
        flag2 = False
print("my_list is a palindrome?  ", flag, my_list)
print("another_list is a palindrome?  ", flag2, another_list)

print('\np07')
# Flatten a nested list structure
nest = [1, [2, [2, 3]], 4]
flat_list = []


def flatten(nest_, flat_list_):
    for i in range(len(nest_)):
        if type(nest_[i]) == list:
            flatten(nest_[i], flat_list_)
        else:
            flat_list_.append(nest_[i])


flatten(nest, flat_list)
print(nest)
print(flat_list)

print('\np08')
# Eliminate consecutive duplicates of list elements
dups = ("a", "a", "a", "a", "b", "c", "c", "a", "a", "d", "e", "e", "e", "e")
compressed = [""]
for i in dups:
    compressed.append(i)
    if compressed[-1] == compressed[-2]:
        compressed.pop(-1)
compressed.pop(0)
print(dups, "\n", compressed)

print('\np09')
# Pack consecutive duplicates of list elements into sub lists
# ie, (A A A A) (B) (C C) (A A) (D) (E E E E)
dups = ("a", "a", "a", "a", "b", "c", "c", "a", "a", "d", "e", "e", "e", "e")
packed = [[""]]
for i in dups:
    if i == packed[-1][0]:  # if the same, then add to the sub list
        packed[-1].append(i)
    else:  # if not then same, then make a new sub list and add it
        packed.append(list(i))
packed.pop(0)
print(dups)
print(packed)
