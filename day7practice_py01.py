#dictionary comprehension ------strip(),sprit()
s="""
practice problems for list com per hension in python.
"""
word_l=s.split(' ')        # convert single words in a total string
print(word_l)
word_l=[i.strip("\n") for i in word_l]       #ignore the \n space which is used in
                                                             #multiple line of srting
print(word_l)
ans={ i: len(i) for i in word_l}     # dictionary comprehession [id:val]
print(ans)
