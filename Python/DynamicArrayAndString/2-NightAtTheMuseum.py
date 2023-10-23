# https://codeforces.com/problemset/problem/731/A
def CalculateMinRotation(inputString):
    minRotation = 0
    pointerPosition = 97
    arrayOfChar = [char for char in inputString]
    for char in arrayOfChar:
        currentVal = ord(char)
        if(pointerPosition == currentVal):
            minRotation = minRotation
        else:
            rightRotation = currentVal - pointerPosition
            leftRotation = pointerPosition - currentVal
            if(rightRotation < 0 ):
                rightRotation = rightRotation + 26
            if(leftRotation < 0):
                leftRotation = leftRotation + 26
            tempMinRotation = min(rightRotation, leftRotation)
            minRotation = minRotation + tempMinRotation
        pointerPosition = currentVal
    return minRotation

inputString = input()
result = CalculateMinRotation(inputString)
print(result)
