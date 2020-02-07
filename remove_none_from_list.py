# -*- coding: utf-8 -*-
"""
@author : yKRSW
@purpose: Sample of remove none from list
"""

list_a = [0, 1, 2, 3, None, 5, 6, 7]
print(list_a)
# [0, 1, 2, 3, None, 5, 6, 7]

print()

list_a_filtered = filter(None, list_a)
print(list_a_filtered)
print(list(list_a_filtered))
# <filter object at 0x0000025F40A48358>
# [1, 2, 3, 5, 6, 7]

print()

list_a_filtered = filter(lambda a:a is not None, list_a)
print(list(list_a_filtered))
# [0, 1, 2, 3, 5, 6, 7]

print()

list_a_filtered = [x for x in list_a if x]
print(list_a_filtered)
# [1, 2, 3, 5, 6, 7]

print()

list_a_filtered = [x for x in list_a if x is not None]
print(list_a_filtered)
# [0, 1, 2, 3, 5, 6, 7]

