with open("madlibs.txt", "r") as file:
    story = file.read()

parts_of_speech = set()

for i in story.split(" "):
    if i.startswith("(") and i.endswith(")"):
        parts_of_speech.add(i)
answers = {}

for word in parts_of_speech:
    user_input = input(f"Enter a word for {word}:")
    answers[word] = user_input

for word in parts_of_speech:
    story = story.replace(word, answers[word])
print(story)
