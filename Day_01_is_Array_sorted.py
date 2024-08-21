def is_array_sorted():
    ele = [1,3,3,10,11]
    count = 0
    try:
        for i in range(len(ele)-1):
            if ele[i] < ele[i+1]:
                continue
            elif ele[i] == ele[i+1]:
                continue
            else:
                count = count + 1
        if count ==0:
            print("Array is Sorted")
        else:
            print("Array is not Sorted")
    except Exception as e:
        print("Some Exception occured",e)

is_array_sorted()
