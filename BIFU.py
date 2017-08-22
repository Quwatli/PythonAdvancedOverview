from functools import reduce
"""
Function that takes a sentence/phrase
breaks it into words then returns the length of each word
in a new list using advanced built in function map()
"""


def word_len(words):

    return list(map(len, words.split()))

print(word_len("Test out this string of words to return length of each word in a list"))

"""
Function using advanced built in function reduce to reduce the list of integers passed 
into a single multi digit number with out directly concatenating to string
"""
print("\n")

def reduce_to_single_digit(lis):

    return reduce(lambda x, y: x*10 + y, lis)

print(reduce_to_single_digit([5, 5, 8, 9, 1]))

"""
Using zip function to concatenate from two lists separating with a specified connector
"""
print("\n")


def conc(e1, e2, sep):

    return [w1 + sep + w2 for (w1, w2) in zip(e1, e2)]

print(conc(['a', 'b'], ['c', 'd'], '+'))

"""
Enumerate to return elements with indexes 
"""
print("\n")


def dict_lis(lis):

    return {k: v for k, v in enumerate(lis)}

print(dict_lis(['a', '2', 'x']))

"""
enumerate to return the count of elements that explicitly correspond to their index
"""
print("\n")


def num_match_index(lis):

    return len([n for x, n in enumerate(lis) if n == x])

print(num_match_index([0, 5, 8, 9, 8, 5, 1, 7, 8, 5]))




