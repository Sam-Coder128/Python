############################################################################################################################
#
# Program      : Filter-Map-Reduce Range Demo
# Functions    : (lambda for filter, lambda for map, lambda for reduce)
# Input        : [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
# Output       : Filter → [76, 89, 86, 90, 70] , Map → [86, 99, 96, 100, 80] , Reduce → 6538752000
# Description  : Filters numbers between 70 and 90, maps by adding 10, reduces by product.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

from functools import reduce

numbers = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]

filtered = list(filter(lambda x: x >= 70 and x <= 90, numbers))
print("List after filter:", filtered)

mapped = list(map(lambda x: x + 10, filtered))
print("List after map:", mapped)

product = reduce(lambda a, b: a * b, mapped)
print("Output of reduce:", product)

###############################################################################################################################
#
# Application : Demonstrates filter-map-reduce pipeline with range conditions.
#
################################################################################################################################
