def interchaing_1_with_2(n):
    n=str(n)
    n=n.replace('1','.')
    n=n.replace('2','1')
    n=n.replace('.','2')
    return n

n=int(input())
print(interchaing_1_with_2(n))
    
