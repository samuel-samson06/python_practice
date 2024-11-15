word = "abcdcdc"
substring = "cdc"
while_loopTrigger = 0
count = 0
length_word = len(word)
length_substring = len(substring)

# since the while loop isn't Up to the length of the passed in word it'll keep running
while while_loopTrigger != length_word:
    # Slices the word string from the current integer of the while loop till the end e.g [ABCDCDC] [BCDCDC] ...
    current_word = word[while_loopTrigger:]
    # Compares the current word by slicing it from the length of the substring
    check_substring = current_word[0:length_substring]
    if check_substring == substring:
        count += 1
    while_loopTrigger += 1
    # print(current_word)
print(count)