from itertools import permutations, combinations, product, combinations_with_replacement

data = ['A', 'B', 'C']

#순열    : permutations
#조합    : combinations
#중복순열 : product
#중복조합 : combinations_with_replacement

print(list(permutations(data, 2)))
print(list(combinations(data, 2)))
print(list(product(data, repeat=2)))
print(list(combinations_with_replacement(data, 2)))