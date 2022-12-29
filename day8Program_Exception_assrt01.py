#exception handaling kelvin should positive numbers
#but to handle to tha negitive numbers use assert keyword
def kelvinToFahreheit(Temprerature):
    assert (Temprerature>=0),"colder then absolute zero at MTICA !"
    res=((Temprerature-273)*1.8)+32
    return res
try:
    print(kelvinToFahreheit(-50))
except Exception as ob:
    print(ob)
try:
    print(kelvinToFahreheit(273))
except Exception as ob:
    print(ob)
try:
    print(kelvinToFahreheit(505.78))
except Exception as ob:
    print(ob)
try:
    print(kelvinToFahreheit(-5))
except Exception as ob:
    print(ob)

print('thank you')
