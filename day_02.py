def greet(instr):
    
    outstr="hello"+" "+instr
    #return outstr.upper()
    return outstr.title()
    #return outstr.lower()
inp=input()
print(greet(inp))
