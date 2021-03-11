from BitVector import *
import math
import timeit
import time
Sbox = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
)

InvSbox = (
    0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
    0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
    0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
    0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
    0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
    0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
    0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
    0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
    0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
    0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
    0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
    0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
    0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
    0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
    0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D,
)

Mixer = [
    [BitVector(hexstring="02"), BitVector(hexstring="03"), BitVector(hexstring="01"), BitVector(hexstring="01")],
    [BitVector(hexstring="01"), BitVector(hexstring="02"), BitVector(hexstring="03"), BitVector(hexstring="01")],
    [BitVector(hexstring="01"), BitVector(hexstring="01"), BitVector(hexstring="02"), BitVector(hexstring="03")],
    [BitVector(hexstring="03"), BitVector(hexstring="01"), BitVector(hexstring="01"), BitVector(hexstring="02")]
]

InvMixer = [
    [BitVector(hexstring="0E"), BitVector(hexstring="0B"), BitVector(hexstring="0D"), BitVector(hexstring="09")],
    [BitVector(hexstring="09"), BitVector(hexstring="0E"), BitVector(hexstring="0B"), BitVector(hexstring="0D")],
    [BitVector(hexstring="0D"), BitVector(hexstring="09"), BitVector(hexstring="0E"), BitVector(hexstring="0B")],
    [BitVector(hexstring="0B"), BitVector(hexstring="0D"), BitVector(hexstring="09"), BitVector(hexstring="0E")]
]

def stringToAsciiMatrix16CharRowMajor(inputString):
    n = 4
    keyMatrix = []
    for i in range(n):
        t = []
        for j in range(n):
            t.append(0)
        keyMatrix.append(t) 
    # print(keyMatrix)


    stringIndex = 0
    for i in range(n):
        for j in range(n):
            # print(i,j)
            
            # print(stringIndex)
            # print(ord(inputString[stringIndex]))
            keyMatrix[i][j] = ord(inputString[stringIndex])
            # print(keyMatrix)
            stringIndex += 1
    # print(keyMatrix)
    return keyMatrix

def stringToAsciiMatrix16CharColumnMajor(plainText):
    n = 4
    stateMatrix = []
    for i in range(n):
        t = []
        for j in range(n):
            t.append(0)
        stateMatrix.append(t) 

    stringIndex = 0
    for i in range(n):
        for j in range(n):
            # print(i,j)
            
            # print(stringIndex)
            # print(ord(inputString[stringIndex]))
            stateMatrix[j][i] = ord(plainText[stringIndex])
            # print(keyMatrix)
            stringIndex += 1
    return stateMatrix

def sBoxSub(w3):
    n = len(w3)
    g = [] 
    for i in range(n):
        val = w3[i]
        # print(val,bin(val))
        rightNibble = (val & 15) #0000 1111 = 15
        # print(val,bin(val))
        leftNibble = (val & 240) >> 4 #1111 0000 = 240 
        # print(val,bin(val))
        # print(leftNibble,bin(leftNibble),rightNibble,bin(rightNibble))
        # print(hex(val))
        # print(hex(leftNibble),hex(rightNibble))
        sBoxValue = Sbox[leftNibble*16+rightNibble]
        g.append(sBoxValue)
    return g

def invSboxSub(w3):
    n = len(w3)
    g = [] 
    for i in range(n):
        val = w3[i]
        # print(val,bin(val))
        rightNibble = (val & 15) #0000 1111 = 15
        # print(val,bin(val))
        leftNibble = (val & 240) >> 4 #1111 0000 = 240 
        # print(val,bin(val))
        # print(leftNibble,bin(leftNibble),rightNibble,bin(rightNibble))
        # print(hex(val))
        # print(hex(leftNibble),hex(rightNibble))
        invSboxValue = InvSbox[leftNibble*16+rightNibble]
        g.append(invSboxValue)
    return g

def hexPrint(list):
    returnStr = ""
    for item in list:
        returnStr = returnStr + str(hex(item))+", "
    return returnStr

def doubleRoundConstant(roundConstant):
    AES_modulus = BitVector(bitstring='100011011')
    bv1 = BitVector(hexstring="02")
    str1 = hex(roundConstant[0])
    str2 = ""
    for i in range(len(str1)-2): # removing Ox before hex string representation
        str2 = str2 + str1[2+i]
    #print(str2)
    #print(str1)
    bv2 = BitVector(hexstring=str2)
    bv3 = bv1.gf_multiply_modular(bv2, AES_modulus, 8)
    #print(bv3)
    roundConstant[0] = bv3.int_val()

def reverseMatrix(matrix):
    n = len(matrix)
    returnMatrix = []
    for i in range(n):
        t = []
        for j in range(len(matrix[0])):
            t.append(0)
        returnMatrix.append(t)
    for i in range(n):
        for j in range(len(matrix[0])):
            returnMatrix[i][j] = matrix[j][i]
    return returnMatrix

def matrixHexPrint(matrix):
    for item in matrix:
        print(hexPrint(item))

def roundKeyGeneration(keyMatrix):
    n=len(keyMatrix)
    roundKeys = []
    # print('hello')
    for item in keyMatrix:
        roundKeys.append(item)
        # print(hexPrint(item))
    # print('hello')

    # print(type(hex(3)))
    roundConstant = [1,0,0,0]

    for round in range(10):
        w3 = roundKeys[-1].copy()
        t = w3[0]
        for i in range(n):
            w3[i] = w3[((i+1)%n)]
        w3[n-1] = t
        #print(hexPrint(w3))
        g = sBoxSub(w3)    
        for i in range(len(g)):
            g[i] = roundConstant[i] ^ g[i]
            # print(hex(g[i]))
        doubleRoundConstant(roundConstant)
        #print(hexPrint(roundConstant))
        w4 = []
        for i in range(n):
            w4.append(roundKeys[-4][i]^ g[i])
            # print(hex(w4[i]))
        #print(hexPrint(w4))
        roundKeys.append(w4)
        for i in range(n-1):
            w = []
            for j in range(n):
                w.append(roundKeys[-1][j] ^ roundKeys[-4][j])
            roundKeys.append(w)
    # print('hi')
    # for item in roundKeys:
    #     print(hexPrint(item))
    # print('hi')

    roundKeys3D = []
    for round in range(int(len(roundKeys)/4)):
        t = []
        for i in range(n):
            t.append(roundKeys[round*4+i].copy())
        # print(round)
        # print(t)
        t =reverseMatrix(t)
        # print(t)
        roundKeys3D.append(t)
    # print('hello')
    # for item in roundKeys3D:
    #     for row in item:
    #         print(hexPrint(row))
    # print('hello')
    roundKeys = roundKeys3D
    return roundKeys

def addRoundKey(stateMatrix,keyMatrix):
    n=len(stateMatrix)
    for i in range(n):
        
        # print(i)
        # print(hexPrint(stateMatrix[i]))
        # print(hexPrint(roundKeys[rowIndex]))
        for j in range(n):
            stateMatrix[i][j] = stateMatrix[i][j] ^ keyMatrix[i][j]

def encryption16Char(stateMatrix,roundKeys):
    



    n=len(stateMatrix)
    addRoundKey(stateMatrix,roundKeys[0])
    # matrixHexPrint(stateMatrix)

    # print('hey')
    for round in range(10):
        
            # print(hexPrint(stateMatrix[i]))

        for i in range(n):
            stateMatrix[i] = sBoxSub(stateMatrix[i])
            # print(hexPrint(stateMatrix[i]))
        # matrixHexPrint(stateMatrix)   
        # for row in stateMatrix:
        #     print(hexPrint(row))

        for i in range(n):
            w = stateMatrix[i]
            # print(i)
            # print(hexPrint(stateMatrix[i]))
            for k in range(i):
                
                t = w[0]
                for j in range(n):
                    w[j] = w[((j+1)%n)]
                w[n-1] = t


        # stateMatrix = reverseMatrix(stateMatrix)
        # matrixHexPrint(stateMatrix)
        if round+1 != 10:
            newMatrix = []
            for row in range(n):
                t = []
                for col in range(n):
                    sum = 0
                    for i in range(n):
                        bv1 = Mixer[row][i]
                        num2 = stateMatrix[i][col]
                        # print(type(num1))
                        # print(type(num2))
                        str2 = hex(num2)
                        str2Prime = ""
                        for j in range(len(str2)-2):
                            str2Prime += str2[j+2]
                        AES_modulus = BitVector(bitstring='100011011')
                        bv2 = BitVector(hexstring=str2Prime)
                        bv3 = bv1.gf_multiply_modular(bv2, AES_modulus, 8)
                        sum = sum ^ bv3.int_val()
                        # print(row,col,hex(bv1.int_val()),hex(bv2.int_val()),hex(bv3.int_val()))
                    # print(row,col,hex(sum))
                    t.append(sum)
                newMatrix.append(t)
            # print('hey')
            # print(matrixHexPrint(newMatrix))
            stateMatrix = newMatrix
        # print('after mix columns round',round+1)
        # matrixHexPrint(stateMatrix)

        addRoundKey(stateMatrix,roundKeys[round+1])
        # print('after roundkey round',round+1)
        # matrixHexPrint(stateMatrix)
    return stateMatrix

def decrypttion16Char(stateMatrix,roundKeys):
    n = len(stateMatrix)
    addRoundKey(stateMatrix,roundKeys[-1])


    for round in range(10):#range(10,0,-1):
        
            # print(hexPrint(stateMatrix[i]))

        
            # print(hexPrint(stateMatrix[i]))
        # matrixHexPrint(stateMatrix)   
        # for row in stateMatrix:
        #     print(hexPrint(row))
        # print('before inverse row shift')
        # matrixHexPrint(stateMatrix)
        for i in range(n):
            w = stateMatrix[i]
            # print(i)
            # print(hexPrint(stateMatrix[i]))
            for k in range(i):
                
                t = w[n-1]
                for j in range(n-1,-1,-1):
                    w[j] = w[((j-1))]
                w[0] = t
        # print('after inverse shift row')
        # matrixHexPrint(stateMatrix)
        for i in range(n):
            stateMatrix[i] = invSboxSub(stateMatrix[i])
        # print('after invsbox')
        # matrixHexPrint(stateMatrix)

        addRoundKey(stateMatrix,roundKeys[-2-round])

        # print('after add round key')
        # matrixHexPrint(stateMatrix)

        if round+1 != 10:
            newMatrix = []
            for row in range(n):
                t = []
                for col in range(n):
                    sum = 0
                    for i in range(n):
                        bv1 = InvMixer[row][i]
                        num2 = stateMatrix[i][col]
                        # print(type(num1))
                        # print(type(num2))
                        str2 = hex(num2)
                        str2Prime = ""
                        for j in range(len(str2)-2):
                            str2Prime += str2[j+2]
                        AES_modulus = BitVector(bitstring='100011011')
                        bv2 = BitVector(hexstring=str2Prime)
                        bv3 = bv1.gf_multiply_modular(bv2, AES_modulus, 8)
                        sum = sum ^ bv3.int_val()
                        # print(row,col,hex(bv1.int_val()),hex(bv2.int_val()),hex(bv3.int_val()))
                    # print(row,col,hex(sum))
                    t.append(sum)
                newMatrix.append(t)
            # print('hey')
            # print(matrixHexPrint(newMatrix))
            stateMatrix = newMatrix
        # print('after invmix columns round',round+1)
        # matrixHexPrint(stateMatrix)

        
        # print('after roundkey round',round+1)
        # matrixHexPrint(stateMatrix)
    return stateMatrix

def stringToASCII(inputString):
    retString = ""
    for c in inputString:
        tempString = hex(ord(c))
        for i in range(len(tempString)-2):
            retString += tempString[2+i]
        retString += " "
    return retString

def matrixToHexStringColumnMajor(matrix):
    retString = ""
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            tempString = hex(matrix[j][i])
            for k in range(len(tempString)-2):
                retString += tempString[2+k]
            retString += " "
    return retString

def matrixToStringColumnMajor(matrix):
    retString = ""
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            retString += chr(matrix[j][i])
    return retString

def keyStringSlice(inputString):
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
    return inputString

def intListToString(intList):
    retString = ""
    for entry in intList:
        retString += chr(entry)
    return retString

def stringTest():
    # inputString = "Thats my Kung Fu"
    # plainText = "Two One Nine Two"
    inputString = input('please enter encryption key:\n')
    plainText = input('please input plaintext to encrypt:\n')


    inputString = keyStringSlice(inputString)



    

    print('Key:')
    print(inputString,'[In ASCII]')
    print(stringToASCII(inputString),'[In HEX]')
    print()
    print('Plain Text:')
    print(plainText,'[In ASCII]')
    print(stringToASCII(plainText),'[In HEX]')

    time5 = timeit.default_timer()
    keyMatrix = stringToAsciiMatrix16CharRowMajor(inputString)
    roundKeys = roundKeyGeneration(keyMatrix)
    time6 = timeit.default_timer()

    totalIterationNeeded = len(plainText)/len(inputString)

    # print(totalIterationNeeded)

    totalIterationNeeded = math.ceil(totalIterationNeeded)
    
    # print(totalIterationNeeded)

    fullText = plainText
    incryptedMatrcies = [] # store matrix of each round

    



    time1 = timeit.default_timer()

    for i in range(totalIterationNeeded):
        plainText = ""
        for position in range(16):
            index = i*16+position
            if index < len(fullText):
                plainText += fullText[index]
            else:
                plainText += " "
        
        
        stateMatrix = stringToAsciiMatrix16CharColumnMajor(plainText)
        stateMatrix = encryption16Char(stateMatrix,roundKeys)

        incryptedMatrcies.append(stateMatrix)
    
    time2 = timeit.default_timer()
    
    cipheredHex = ""
    for matrix in incryptedMatrcies:
        cipheredHex += matrixToHexStringColumnMajor(matrix)
    
    cipheredText = ""
    for matrix in incryptedMatrcies:
        cipheredText += matrixToStringColumnMajor(matrix)
     
    

    print('Cipher Text:')
    print(cipheredHex,'[In HEX]')
    print(cipheredText,'[In ASCII]')

    time3 = timeit.default_timer()
    decryptedMatrcies = []
    for matrix in incryptedMatrcies:
        stateMatrix = decrypttion16Char(matrix,roundKeys)
        decryptedMatrcies.append(stateMatrix)
    time4 = timeit.default_timer()

    decipheredHex = ""
    for matrix in decryptedMatrcies:
        decipheredHex += matrixToHexStringColumnMajor(matrix)
    
    decipheredText = ""
    for matrix in decryptedMatrcies:
        decipheredText += matrixToStringColumnMajor(matrix)
     
    

    print('Decipher Text:')
    print(decipheredHex,'[In HEX]')
    print(decipheredText,'[In ASCII]')
    
    print()
    print('Execution Time')
    print('Key Scheduling:',time6-time5)
    print('Encryption Time:',time2-time1)
    print('Decryption Time:',time4-time3)
    

    # stateMatrix = decrypttion16Char(stateMatrix,roundKeys)

    # print('Deciphered Text:')
    # print(matrixToHexStringColumnMajor(stateMatrix),'[In HEX]')
    # print(matrixToStringColumnMajor(stateMatrix),'[In ASCII]')


    # matrixHexPrint(stateMatrix)

def list1DToList2DColumnMajor(myList):
    list2D = []
    length = int(math.sqrt(len(myList)))
    for i in range(length):
        list2D.append([0]*length)
    for i in range(length):
        for j in range(length):
            list2D[j][i] = myList[i*length+j]
    return list2D

def list2DColumnMajorToList1D(myList2D):
    retList = []
    for i in range(len(myList2D[0])):
        for j in range(len(myList2D)):
             retList.append(myList2D[j][i])
    return retList

def encryptFile(): 
    keyString = input('please enter encryption key:\n')
    keyString = keyStringSlice(keyString)

    inputFileName = input('please enter input file name:\n')
    currentTime = int(time.time())
    outputFileName = "E"+str(currentTime)
    
    keyMatrix = stringToAsciiMatrix16CharRowMajor(keyString)
    roundKeys = roundKeyGeneration(keyMatrix)
    
    
    # print(int(time.time()))
    # print(timeit.default_timer())
    bytesRead = 0
    f = open(inputFileName, "rb")
    outputFile = open(outputFileName,"ab")
    bytes = f.read(16)
    while len(bytes)>0 :
        # print(len(bytes))
        bytesRead += len(bytes)
        intForm16 = [ord(' ')]*16 #appending 16 space
        # print(len(intForm16))
        # print(type(bytes[0]))
        # print(bytes[0])
        for i in range(len(bytes)):
            intForm16[i] = bytes[i]
        
        # plainText = intListToString(intForm16)
        # stateMatrix = stringToAsciiMatrix16CharColumnMajor(plainText)
        stateMatrix = list1DToList2DColumnMajor(intForm16)
        stateMatrix = encryption16Char(stateMatrix,roundKeys)
        # outText = matrixToStringColumnMajor(stateMatrix)
        outList = list2DColumnMajorToList1D(stateMatrix)
        

        
        outputFile.write(bytearray(outList))
        # print(plainText)
        
        bytes = f.read(16)
    
    f.close()
    outputFile.close()
    
    # outputFile2 = open("EN"+str(currentTime),"ab")
    # outputFile2.write(bytearray(str(bytesRead)+"\n","UTF-8"))
    # outputFile = open(outputFileName,"rb")
    # stringChunk = outputFile.read(100)
    # count = 0
    # while(len(stringChunk)>0):
    #     count += len(stringChunk)
    #     outputFile2.write(stringChunk)
    #     stringChunk = outputFile.read(100)
    # print(count)


        
    
    # print('under construction!')

def decryptFile():
    keyString = input('please enter decryption key:\n')
    keyString = keyStringSlice(keyString)

    inputFileName = input('please enter input file name:\n')
    currentTime = int(time.time())
    outputFileName = "D"+str(currentTime)+inputFileName
    
    keyMatrix = stringToAsciiMatrix16CharRowMajor(keyString)
    roundKeys = roundKeyGeneration(keyMatrix)
    
    
    # print(int(time.time()))
    # print(timeit.default_timer())
    firstLine = True
    
    f = open(inputFileName, "rb")
    outputFile = open(outputFileName,"ab")
    # bytesToBeRead = 0
    # if firstLine:
    #     bytesToBeRead = int(f.readline())
    
    # readSoFar = 0
    bytes = f.read(16)
    while len(bytes)>0 :
        # readSoFar += len(bytes)
        # print(len(bytes))
        intForm16 = [ord(' ')]*16 #appending 16 spaces
        # print(len(intForm16))
        # print(type(bytes[0]))
        # print(bytes[0])
        for i in range(len(bytes)):
            intForm16[i] = (bytes[i])
        


        stateMatrix = list1DToList2DColumnMajor(intForm16)
        stateMatrix = decrypttion16Char(stateMatrix,roundKeys)
        outList = list2DColumnMajorToList1D(stateMatrix)
        
        # if readSoFar>bytesToBeRead:
        #     dif = readSoFar - bytesToBeRead
        #     tempText = []
        #     for i in range(len(outList)-dif):
        #         tempText.append(outList[i]) 
        #     outList = tempText

        
        outputFile.write(bytearray(outList))
        # print(plainText)
        
        bytes = f.read(16)
    f.close()
    outputFile.close()   
    
    # print('under construction!')

# f = open('reference','rb')
# bytes = f.readline()
# print(type(bytes),type(bytes[0]),bytes[0],bytes.decode("utf-8"))
# print(bytes)
# bytes = f.read(100)
# print(type(bytes),type(bytes[0]),bytes[0],chr(bytes[0]))


choice = -5
try:
    choice = int(input('press 1 for string encryption 2 for file encryption:\n'))
except:
    choice = -5
if choice == 1:
    stringTest()
elif choice == 2:
    choice = (input('press 1 for encrypting file anything else for decrypting file'))
    if(choice == "1"):
        encryptFile()
    else:
        # print('hi')
        decryptFile()
else:
    print('invalid input hence closing the program. restart to try again!\n')

    

# inputString = input("Please insert encryption key(128bit 16byte):")
# print(inputString)



