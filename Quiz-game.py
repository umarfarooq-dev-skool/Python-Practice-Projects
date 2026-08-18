questions = {
    "What is the capital of Pakistan?": "Islamabad",
    "What is 5 + 5?": "10",
    "Which language are you learning?": "Python",
    "How many days are in a week?": "7"
}

score = 0

for question, answer in questions.items():
    print("\n" + question)

    user_answer = input("Answer: ")

    if user_answer.lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print("\nQuiz finished!")
print("Your score:", score, "/", len(questions))