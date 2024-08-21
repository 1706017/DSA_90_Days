def check_string_palindrome():
    try:
        a = input("Enter a string")
        #implementing string slicing in python
        b = a[-1::-1]
        if a==b:
            print("The String",a,"is a Palindrome String")
        else:
            print("The string is not a Palindrome String")
    except Exception as e:
        print("Some Exception")

check_string_palindrome()   
