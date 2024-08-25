def find_missing_number(n):
    arr1 = [1,2,3,5]
    sum_of_natural_numbers = n * (n+1)/2
    sum_array=0
    for i in range(0,len(arr1)):
        sum_array = sum_array+arr1[i]
        
    
    missing_number = sum_of_natural_numbers - sum_array
    print("The missing number from array is ",missing_number)

find_missing_number(5)

OUTPUT:
      The missing number from array is 4
