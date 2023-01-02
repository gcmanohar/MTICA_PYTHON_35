#one string and one dictonary  merging to distonary
empls=['manohar','ganguly','arun']
defalt_v={"designation":'developer',"salary":80000}
data=dict.fromkeys(empls,defalt_v)
print(data)

#indiviual
print(data["manohar"])
