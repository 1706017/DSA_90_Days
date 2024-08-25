def linear_search(num):
    arr = [1,2,3,67,89,90]
    print("The number that you have entered for serach is ",num)
    count=0
    for i in range(0,len(arr)-1):
        if arr[i]==num:
            print("Your numn is found at index",i)
            count=count+1
            break
        else:
            continue
    if count==0:
        print("Sorry your number does not exists in array")
        
    

linear_search(999)
