# https://codeforces.com/problemset/problem/691/A
def checkJacket(v,n):
  if n == 1:
    if v[0] == 1:
      return True
    else: 
      return False
  count = 0
  for i in range(n):
    if v[i] == 0:
      count += 1
  if count == 1:
    return True
  else:
  	return False

print("please enter your input:")  
n = int(input())
v = list(map(int, input().split()))
if checkJacket(v,n):
  print ("YES")
else:
	print ("NO")
