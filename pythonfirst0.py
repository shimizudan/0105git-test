import itertools

# list(itertools.permutations(range(4) ) )

print(list(itertools.permutations(range(7) ) ) )
# print('permutations(range(4), 2): ', list(itertools.permutations(range(4), 2 ) ) )

seq = ('a', 'b', 'c', 'd', 'e')

list(itertools.permutations(seq))
len(list(itertools.permutations(seq)))
list(itertools.permutations(seq, 3))
len(list(itertools.permutations(seq, 3)))
list(itertools.combinations(seq,5))

list(itertools.combinations(seq,3))
len(list(itertools.combinations(seq,3)))

list(itertools.product(seq, seq))
len(list(itertools.product(seq, seq)))

list(itertools.product(seq, repeat=3))
len(list(itertools.product(seq, repeat=3)))

list(itertools.combinations_with_replacement(seq, 3))
len(list(itertools.combinations_with_replacement(seq, 3)))
