def reverse_word(s):
    
    split_word = s.split()
    print(type(split_word))
    print((split_word))

    split_word.reverse()
    print(split_word)


sentence = input("Enter the string : ")
print("This is string value  :" + sentence)

reverse_word(sentence)