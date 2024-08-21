def find_second_largest_element():
    try:
        ele = [12,18,67,90,90,87]
        first_large = ele[0]
        for i in ele:
            if i > first_large:
                first_large = i
            else:
                continue
        #Assuming our array does not contain -ve value
        second_large = -1
        for i in ele:
            if i > second_large and i != first_large:
                second_large = i
            else:
                continue
        
        print("First Large Element in the array is ",first_large)
        print("Second Large Element in the array is ",second_large)
    except Exception as e:
        print("Some Exception has occured",e)

find_second_largest_element()
