import sys
from random import *
def getR():
    return randint(
        -sys.maxsize ** 2,
        sys.maxsize ** 2
    )
curVal = 'no value yet'
for iter in range(333):
    if input('press any key: ') == 'exit':
        break
    curVal = getR()
    valStr = str(curVal)
    finalVal = ''
    l = len(valStr)
    for i in range(len(valStr)):
        if l % 3 == 0:
            finalVal += ' '
        l-=1
        finalVal += valStr[i]
    print(finalVal)