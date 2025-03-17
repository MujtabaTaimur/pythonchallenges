def main():
    
    questions = [
        "What is the capital of France?",
        "What is 2 + 2?",
        "What is the color of the sky on a clear day?"
    ]
    answers = [
        "Paris",
        "4",
        "Blue"
    ]
    score = 0
    
 
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    33weeee12e

    for i in range(len(questions)):
        user_answer = input(questions[i] + " ")
        if user_answer.strip().lower() == answers[i].strip().lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
    
   
    print(f"\n{name}, your score is {score}/{len(questions)}")

if __name__ == "__main__":
    main()

