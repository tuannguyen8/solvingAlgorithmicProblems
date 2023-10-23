# https://codeforces.com/problemset/problem/242/B

# print("hello")
def findBigSegment(numOfSegment):
    left,right = [],[]
    for _ in range (numOfSegment):
        a,b = map(int, input().split())
        left.append(a)
        right.append(b)
    l,r = min(left), max(right)

    for i in range (numOfSegment):
        if l == left[i] and r == right[i]:
            return i+1
       
    return -1
numOfSegment = int(input())
result = findBigSegment(numOfSegment)
print(result)

