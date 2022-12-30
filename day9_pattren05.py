#tringle pattres problems
def PrintSerie(sy,n):
    sp=' . '
    for i in range(0,n):
        print(sp*(n-i-1)+sy*(2*i+1)+sp*(n-i-1))
    return None
sy=input()
n=int(input())
PrintSerie(sy,n)

#output
*
5
 . . . .* . . . .
 . . .*** . . .
 . .***** . .
 .******* .
*********
