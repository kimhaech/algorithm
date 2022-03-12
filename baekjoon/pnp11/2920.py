li = list(map(int, input().split()))

t = [[1,2,3,4,5,6,7,8],[8,7,6,5,4,3,2,1]]

if li[0] == 1:
  for i in range(len(li)):
    if li[i] == t[0][i]:
      temp = 'ascending'
    else:
      temp = 'mixed'
      break
elif li[0] == 8:
  for i in range(len(li)):
    if li[i] == t[1][i]:
      temp = 'descending'
    else:
      temp = 'mixed'
      break
else:
  temp='mixed'

print(temp)
