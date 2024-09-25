import random
import time

START_RANDOM_NUMBERS = 3
END_RANDOM_NUMBERS = 20
WHILE_TRIGGER = 10
TOTAL_QUESTIONS = 0
NUMBER_FAILED = 0


def generate_quiz():
    operation = ["+", "-", "*", "/"]
    random_number_start = random.randint(START_RANDOM_NUMBERS, END_RANDOM_NUMBERS)
    random_number_end = random.randint(START_RANDOM_NUMBERS, END_RANDOM_NUMBERS)
    random_operations = random.choice(operation)
    question = f"{int(random_number_start)} {random_operations} {int(random_number_end)}"
    result = eval(f"{int(random_number_start)} {random_operations} {int(random_number_end)}")
    return question, result


START_TIME = time.time()
while WHILE_TRIGGER > 0:
    calculation, answer = generate_quiz()
    print(calculation)
    user_answer = float(input("Enter Your Answer::"))
    if user_answer == round(answer, 3):
        WHILE_TRIGGER -= 1
    else:
        NUMBER_FAILED += 1
        print("Failed")
    TOTAL_QUESTIONS += 1
END_TIME = time.time()
print(f"Number of Questions Asked {TOTAL_QUESTIONS}")
print(f"You Failed {NUMBER_FAILED}")
print(f"Total time taken to answer is {round(END_TIME-START_TIME, 2)} seconds")
