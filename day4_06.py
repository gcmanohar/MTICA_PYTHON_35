def interchaing3_5(n):
    n=str(n)
    n=n.replace('3','.')
    n=n.replace('5','3')
    n=n.replace('.','5')
    return n

n=int(input())
print(interchaing3_5(n))
    
