arr = list(map(int, input('Enter your list:\n').split(',')))
flag=True
for i in range(len(arr)):
    if arr[i]!=arr[len(arr)-1-i]:
        flag=False
        break
if flag:
    print('the list is symmetric')
else:
    print('the list is not symmetric')