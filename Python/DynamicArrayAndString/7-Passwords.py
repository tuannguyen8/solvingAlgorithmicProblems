# https://codeforces.com/problemset/problem/721/B

def passwordData(n):
    countArray = [0]*101
    for i in range(n):
        password = input()
        countArray[len(password)] += 1
    return countArray

def calculateTime(countArray, lenOfPassword,k):
    bestTime = 0
    worstTime = 0
    tempTime = 0
    for i in range(lenOfPassword):
        tempTime += countArray[i]

    bestTime = tempTime//k*5 + tempTime + 1
    worstTime = (tempTime + countArray[lenOfPassword] - 1)//k*5 + (tempTime + countArray[lenOfPassword]-1) + 1
    print(bestTime, worstTime, sep = ' ')

n, k = map(int, (input().split()))
countArray = passwordData(n)
VaynaPassword = input()
lenOfPassword = len(VaynaPassword)
calculateTime(countArray, lenOfPassword,k)
