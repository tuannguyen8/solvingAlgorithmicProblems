# https://www.hackerearth.com/problem/algorithm/choose-from-two-arrays-eebbddf0-349fa1b7/
def ifTrictlyLessThan (sizeofArray, choosingValue, arrayA, arrayB):
    count = 0
    for i in range(len(arrayB) - 1, -1, -1):
        print(i)
        if(arrayA[choosingValue[0]-1] < arrayB[i]):
            count += 1
            print(count)
            if(count >= choosingValue[1]):
                return print("YES")
    return print("NO")

sizeOfArray = list(map(int, input().split()))
choosingValue = list(map(int, input().split()))
arrayA = list(map(int, input().split()))
arrayB = list(map(int, input().split()))

ifTrictlyLessThan(sizeOfArray, choosingValue, arrayA, arrayB)

# 0. check if there is enough value in arrayB to compare choosingValue[0] times.
# 1. comparing arrayA[choosingValue[0]] to each value in arrayB
# 2. if arrayA[choosingValue[0]] is smaller than value in arrayB, then increase count++
# 3. if count is equal or greater than choosingValue[1] then return "YES", else return "NO"
