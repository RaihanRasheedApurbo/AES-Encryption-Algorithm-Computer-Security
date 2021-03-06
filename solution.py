inputString = input("Please insert encryption key(128bit 16byte):")
# print(inputString)

if(len(inputString)<16):
    i = len(inputString)
    while(i!=16):
        inputString = inputString + " "
        i += 1
elif(len(inputString)>16):
    newString = ""
    i = 0
    while(i!=16):
        newString += inputString[i]
        i += 1
    inputString = newString
# print(inputString)
# print(len(inputString))
