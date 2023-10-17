# https://codeforces.com/problemset/problem/673/A
def watchingTime(numOfInteresting, listOfMinutes):
    watchingMinutes = 0
    
    for i in range(numOfInteresting):
        if (watchingMinutes + 15) < listOfMinutes[i]:
            return watchingMinutes + 15
        else:
            watchingMinutes = listOfMinutes[i]

    return min(watchingMinutes+15,90)

numOfInteresting = int(input())
listOfMinutes = list(map(int, input().split()))
result = watchingTime(numOfInteresting, listOfMinutes)
print(result)
