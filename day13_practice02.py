def printBlue():
    print('You chose blue! \n')
def printBlack():
    print('You chose black! \n')
def printRed():
    print('You chose red! \n')
def printYellow():
    print('You chose Yellow! \n')
def choice():
    assert (n>=5), "INVALID"
    print("0: blue")
    print("1: black")
    print("2: red")
    print("3: yello")
    print("4: quick")
    return
colorSelect={ 0: printBlue , 1: printBlack , 2: printRed , 3: printYellow }
selection=0
while True:
    if selection == 4: break
    choice()
    selection= int(input(" select a color option: "))
    if ((selection >=0) and (selection < 4)):
        colorSelect[selection]()
