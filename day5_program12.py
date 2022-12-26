#combination of 0's and 1's
def combine_0_1(s):
    if s<0:
        return "invalid"
    if s>0:
        return s
s1=int(input())
a=combine_0_1(s1)
print('10'*(s1-1)+'1')

#input==6
#output==10101010101
's=int(input())
print('10'*(s-1)+'1')

#input==5
#output==010101010

s=int(input())
print('01'*(s-1)+'0')

#input==5
#output==1000001
s=int(input())
print('1'+'0'*(s)+'1')
