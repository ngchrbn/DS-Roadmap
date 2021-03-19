s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = {3, 4, 5}

# Intersection between s1, s2, s3
s4 = s1.intersection(s2, s3)

# Difference between s1 and s2(items in s1 but not in s2)
s5 = s1.difference(s2)
# symmetric_difference() gives all the items
# that are neither in s1 nor s2(or many sets)
sym_diff = s1.symmetric_difference(s2)


# Union between s1 and s3 (items in s1 and s3)
union = s1.union(s3)
print("Sets:\n", "s1:", s1, "\ns2:", s2, "\ns3:", s3, "\n")
print("s1 inter s2:", s4)
print("s1 | s2:", s5)
print("s1 sysmmetric | s2:", sym_diff)
print("s1 union s2:", union)