def solve(arr):
    left = [0]
    for i in range(1, len(arr)):
        if arr[i]<arr[i-1]:
            left.append(i-1)
        elif arr[i] < arr[left[i-1]]:
            left.append(left[i-1])
        else:
            left.append(left[left[i-1]])

    for i in range(0,len(left)):
        left[i]+=1

    right = [0]
    for j in range(len(arr)-2,-1,-1):
        if arr[j]< arr[j+1]:
            right.insert(0,j+1)
        elif arr[j]<arr[right[0]]:
            right.insert(0,right[0])
        else:
            right.insert(0, right[right[0]-1])
    for i in range(0,len(right)):
        right[i]+=1

    temp = 0
    for i in range(0, len(arr)):
        c = left[i] * right[i]
        if temp < c:
            temp = c

    return temp

print(solve([5,4,3,4,5]))