def union_sorted_array():
    arr1 = [1,1,2,3,3,4,5,10]
    arr2 = [1,2,2,3,3,3,5,6,7,8]
  
    #Initializing the set with emptyset
    union_set = set()
    union_set.update(arr1)
    union_set.update(arr2)
  
    print(union_set)
    
union_sorted_array()


Input: 
    arr1 = [1,1,2,3,3,4,5,10]
    arr2 = [1,2,2,3,3,3,5,6,7,8]
Output:
    [1,2,3,4,5,6,7,8,10]

