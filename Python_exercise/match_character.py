def match_character():
    string1 = input("Enter the 1st character : ")
    string2 = input("Enter the 2nd character : ")
    print(string1)
    print(string2)
    if string2 in string1:
        print("yes")
    else:
        print("no")

match_character()