spins=[('red','18'),('black','13'),('red','12'),('red','40'),('red','50'),
       ('red','14'),('black','1'),('black','40'),('red','18'),('black','40')]
def countReds(lis):
    count=0
    for color,number in lis:
        if color=='black':
            yield count
            count=0
        else:
            count +=1
    yield count
gaps=[i for i in countReds(spins)]
print(gaps)
        
