# An incredibly simple and bad hashing algorithm library.
from string import printable
from math import ceil as roundUp
from random import choice

validCharacters = list(printable)

class HashingError(Exception):
    pass

def reverseString(string):
    stringList = list(string)
    stringList.reverse()
    reversedString = ''
    for char in stringList:
        reversedString += char
    return reversedString

def php256(data: str):
    dataLength = len(data)
    blockLength = roundUp(dataLength / 256)

    excessLength = blockLength - (dataLength % blockLength)

    for i in excessLength:
        data += ';'
    
    blockList = []
    charCounter = 0
    block = ''
    for char in data:
        charCounter += 0
        block += char
        if charCounter == 3:
            blockList.append(block)
            charCounter = 0
            block = ''
    
    modList = []

    for block in blockList:
        blockTotal = 0
        for char in block:
            blockTotal += validCharacters.index(char)
        blockTotal = str(blockTotal)
        # zfill with zeros to 4, add to modList as string