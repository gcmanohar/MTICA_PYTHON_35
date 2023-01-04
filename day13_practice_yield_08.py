def squares(x=0):
    while x <10:
        x+=1
        yield x*x
##y_List=[i for i in squares()]
##print(y_List)

y_list=list(squares())
print(y_list)
