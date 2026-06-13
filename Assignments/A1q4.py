############################################################################################################################
#
# Program      : Memory Size Demo
# Input        : None
# Output       : Prints memory sizes of int, float, str, list, and bool
# Methods      : sys.getsizeof()
# Description  : Demonstrates how Python objects have different memory sizes due to internal overhead.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import sys

print(sys.getsizeof(10))         # int    → 28 bytes
print(sys.getsizeof(3.14))       # float  → 24 bytes
print(sys.getsizeof("hi"))       # str    → 51 bytes
print(sys.getsizeof([1,2,3]))    # list   → 88 bytes
print(sys.getsizeof(True))       # bool   → 28 bytes (bool is subclass of int)

# WHY are sizes different?
# Every Python object has overhead: type pointer, reference count,
# value — that's already ~16–28 bytes before any actual data.
#
# int    → fixed 28 bytes (stores number + object header)
# float  → fixed 24 bytes (64-bit IEEE double + header)
# str    → 49 bytes base + 1 byte per ASCII char
# list   → 56 bytes base + 8 bytes per item slot (pointer size)
# bool   → same as int because bool inherits from int
#
# getsizeof() is useful to understand memory cost,
# but for nested containers it only counts the shell,
# not the objects inside.

###############################################################################################################################
#
# Application : Shows how Python’s sys.getsizeof() reveals memory overhead differences between immutable and mutable objects.
#
################################################################################################################################
