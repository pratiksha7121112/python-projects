questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. London", "B. Paris", "C. Berlin", "D. Romme"],
        "answer": "B"
    },
    {
        "question": "What is the chemical symbol for Gold?",
        "options": ["A. Go", "B. Gd", "C. Au", "D. Ag"],
        "answer": "C"
    },
    {
        "question": "Which is the largest ocean on Earth?",
        "options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
        "answer": "D"
    },
    {
        "question": "Who is known as the founder of Microsoft?",
        "options": ["A. Steve Jobs", "B. Bill Gates", "C. Elon Musk", "D. Mark Zuckerberg"],
        "answer": "B"
    },
    {
        "question": "How many continents are there on Earth?",
        "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
        "answer": "C"
    }
]

score = 0

for question in questions:
    print(question["question"])
    for option in question["options"]:
        print(option)
    while True:
        answer = input("Your answer (A/B/C/D): ").upper()
        if answer in ["A", "B", "C", "D"]:
            break
        else:
            print("Invalid input! Please enter A, B, C or D.")
    if answer == question["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong! Correct answer was", question["answer"])
print("")
print("Your final score:", score, "out of", len(questions))

    


    