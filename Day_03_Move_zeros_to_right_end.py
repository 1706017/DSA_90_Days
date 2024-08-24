def move_zeros_to_right_end():
    arr = [1,2,0,3,5,8,9,0,0,8]
    for i in range(0,len(arr)-1):
        if arr[i] == 0:
            j=i
            break
    
    for i in range(j+1,len(arr)):
        if arr[i]!=0:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            j=j+1
        else:
            continue
    
    for i in range(0,len(arr)):
        print(arr[i])

move_zeros_to_right_end()
