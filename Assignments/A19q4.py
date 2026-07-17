############################################################################################################################
#
# Program      : Filter-Map-Reduce Even Demo
# Input        : [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
# Output       : Filter → [2, 4, 4, 2, 8, 10] , Map → [4, 16, 16, 4, 64, 100] , Reduce → 204
# Description  : Filters even numbers, maps to squares, reduces to sum.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

from functools import reduce

numbers = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]

filtered = list(filter(lambda x: x % 2 == 0, numbers))
print("List after filter:", filtered)

mapped = list(map(lambda x: x * x, filtered))
print("List after map:", mapped)

total = reduce(lambda a, b: a + b, mapped)
print("Output of reduce:", total)

###############################################################################################################################
#
# Application : Demonstrates filter-map-reduce pipeline with even numbers.
#
################################################################################################################################
