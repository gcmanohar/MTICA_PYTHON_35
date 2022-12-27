coor=[(3,9),(2,4)]
print('first tuple: {0[0]}, {0[1]}, second tuple: {1[0]},{1[1]}'.format(*coor))

print('{:#<30}'.format('apple'))   #left aligned
print('{:*>30}'.format('apple'))   # right aligned
print('{:^30}'.format('apple'))  # center--
print('{:*^30}'.format('apple'))   #left aligned

print("int: {0:d}; hex: {0:x}; oct: {0:o}; bin: {0:b}".format(42,55))
print("int: {1:d}; hex: {1:x}; oct: {1:o}; bin: {1:b}".format(42,55))
print('{:,}'.format(1234567890))
p=19.0; t=22
print('currect answers: {:.2%}'.format(p/t))
print('currect answers: {:.2}'.format(p/t))
