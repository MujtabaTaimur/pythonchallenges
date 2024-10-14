def ask_question(question):
 
    print(question[0])
    for i, option in enumerate(question[1:-1], start=1):
        print(f"{i}. {option}")
    user_answer = int(input("Your answer (1/2/3/4): "))
    

    if question[user_answer] == question[-1]:
        print("Correct!")
        return 1
    else:
        print("Incorrect.")
        return 0

def math_quiz():

    questions = [
        ["What is 2 + 2?", "1", "2", "3", "4", "4"],
        ["What is 5 - 3?", "1", "2", "3", "4", "2"],
        ["What is 3 * 3?", "6", "7", "8", "9", "9"]
    ]

    score = 0
    for question in questions:
        score += ask_question(question)
    
    print(f"\nYou scored {score}/{len(questions)}.")


math_quiz()
