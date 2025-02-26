# An incredibly simple and bad hashing algorithm library.
from string import printable

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
    if len(data) > 256:
        raise HashingError('Input is too long')
    
    for char in data:
        if not char in validCharacters:
            raise HashingError('Input contains invalid characters')

    hashableData = data.zfill(256)

    hashedData = []
    for char in data:
        hashedData.append(hex(validCharacters.index(char)))
    
    moreHashedData = []
    for value in hashedData:
        moreHashedData.append(reverseString(value))

    hashedString = ''
    for value in moreHashedData:
        hashedString += value
    
    return hashedString