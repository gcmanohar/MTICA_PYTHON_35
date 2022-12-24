s=[[35,'manohar',86,85],[13,'ganguli',75,89],[44,'prasad',76,77]]
s.sort()
print(s,end=" ")
s.sort(key=lambda t:t[1])
print(s)
s.sort(key=lambda t:t[2])
print(s)
s.sort(key=lambda t:t[3])
print(s)
