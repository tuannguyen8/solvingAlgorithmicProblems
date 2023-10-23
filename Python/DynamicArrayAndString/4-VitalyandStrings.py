# https://codeforces.com/problemset/problem/518/A       
def lookForString(stringS, stringT):
    for i in range(len(stringS) -1 , -1, -1):
        if stringS[i] == 'z':
            stringS[i] = 'a'
        else:
            stringS[i] = chr(ord(stringS[i])+ 1)
            break
        
    if(stringS == stringT):
        print("No such string")
    else:
        print(''.join(stringS))

stringS = list(input())
stringT = list(input())
lookForString(stringS, stringT)