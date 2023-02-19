string1 = "To  24 Pakistan’s east is India, which has a 2912 km border with Pakistan. To its west is Iran, which has a 909 km border with Pakistan. To Pakistan’s northwest lies Afghanistan, with a shared border of 2430 km"

value = string1.split()

for x in value:
    if(x.isdigit()):
        result = (int(x))
        index1 = value.index(x)
        pre_word = value[index1 - 1]
        next_word = value[index1 + 1]

        print("Numbers : ", result)
        print("Index of integers Value : ", index1)
        print("Previous Value  : ", pre_word)
        print("Next Value  : ", next_word)
        print(" ")
        print(" ")





