def reverse_string():
    try:
        a = input("Enter a string :")
        b = a[-1::-1]
        print("The reverse of string is ",b)
    except Exception as e:
        print("There is some exception occured",e)


reverse_string()
