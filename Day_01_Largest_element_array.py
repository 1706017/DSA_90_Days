def find_largest_element():
    try:
        ele = [129,23,98,100,78]
        lar = ele[0]
        for i in ele:
            if i > lar:
                lar = i
            else:
                continue
        print("The Largest element in the list is ",lar)
    except Exception as e:
        print("Some Exception occured")

find_largest_element()
