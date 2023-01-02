month={1:'January ',2:'February ',3:'March ',4:'April ',5:'May ',
       6:'June',7:'July ',8:'August ',9:'September ',10:'October ',
       11:'Nevember ',12:'December ',}
mn=int(input())
if mn>=1 and mn<=12:
    print(month[mn])
else:
    print('INVALID')
