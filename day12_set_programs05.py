#set operations
s1={ 10, 20, 50, 60, 70}
s2={ 30, 40, 50, 60, 70}

if s1.isdisjoint(s2):
    print("two sets have no items in common")
else:
    print("two sets have  items in common")
    print(s1.intersection(s2))

print(s1.symmetric_difference_update(s2)) # remove all commen things
print(s1.intersection_update(s2))   #remove not commen things


