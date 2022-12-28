###remove emty list
ls=['manohar','manu','','','baaru']
ans=[]
for i in ls:
    if i:        # by default T/F boolean operations 
        ans.append(i)
print(ans)

#list comprehension
print([i for i in ls if i])

##for i in range(5):
##    inp=input()
##    if inp:
##        print("hello "+inp)
##    else:
##        print("bye")
