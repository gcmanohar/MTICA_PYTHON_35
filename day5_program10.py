#remove duplicates.......
def remove_duplicates(s):
    st=''
    for i in s:
        if i not in st:
            st+=i
    return st
s1=input()
a=remove_duplicates(s1)
print("removing duplicates : ",a)

'''
s=input()
st=''
for i in s:
    if i not in st:
        st+=i
print("without vowels ",st)
'''
