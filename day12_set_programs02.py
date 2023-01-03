#set operations
s1={ 10, 20, 30, 40, 50}
s2={ 30, 40, 50, 60, 70}

print(s1.intersection(s2))   # commen things
#print(s1.intersection_update(s2))
print(s1.union(s2))         # all things no repatation
# remove duplicates
print(s1 ^ s2)

print(s1.difference_update(s2))    #only one set things not repeting thimgs
