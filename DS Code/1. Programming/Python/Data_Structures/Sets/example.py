# Complexity: O(1)

s1 = set([1, 2, 3, 4, 5])

# To add a new item
s1.add(6)



# To update it with another set
s2 = {7, 8, 9}
s1.update(s2)


# To remove an item (throw an error if the item is not found)
s1.remove(5)

# or using 'discard(item)' => if the item is not found
# it does nothing
s1.discard(10)


print(s1)

0