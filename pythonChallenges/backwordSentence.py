def reverse_word(sentence):
    word_array = []
    for words in sentence:
        word_array.append(words)
    word_array.reverse()
    test = ''.join(word_array)
    split_two = test.split()
    split_two.reverse()
    return ' '.join(split_two)


user_input = input("Enter a sentence to see how the program works:- ")
x = reverse_word(user_input)
print(x)
