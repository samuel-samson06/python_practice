# print("minion")
# Turns word to lower case
word = input("").lower()
# Gets the length of the given word
length_word = len(word)
stuart = 0
kevin = 0
vowels = "AEIOU".lower()
consonants = "BCDFGHJKLMNPQRSTVWXYZ".lower()
# While the word is greater than 0
while length_word > 0:
    # prints a slice of the word based on the current length example from 0-6
    # print(word[0:length_word]) decided to test a slice of the word
    # runs a for loop through the words and adds them to their required individual
    for i in (word[0:length_word]):
        if i in vowels:
            kevin += 1
        else:
            stuart += 1
    # Minuses from the current word length example 6-1=5
    length_word -= 1
if stuart > kevin:
    print(f"Stuart {stuart}")
else:
    print(f"Kevin {kevin}")
