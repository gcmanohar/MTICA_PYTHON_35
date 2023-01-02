#two dictonarys merge one dictonary ------- duplicates not allowed
dict1={ 'ten':10, 'twenty':20 }
dict2={ 'thirty':30,'fourty':40,'ten':10 }
dict3={**dict1,**dict2}

dict4=dict1.copy()     # another mettod
dict4.update(dict2)
print(dict3)

print(dict4)

##output:
##{'ten': 10, 'twenty': 20, 'thirty': 30, 'fourty': 40}
##{'ten': 10, 'twenty': 20, 'thirty': 30, 'fourty': 40}
