def load_scores():
    try:
        with open("scores.txt", "r") as file:
            scores = file.readlines()
            return [score.strip() for score in scores]
    except FileNotFoundError:
        return []  # If the file doesn't exist, return an empty list

def save_score(name, score):
    with open("scores.txt", "a") as file:
        file.write(f"{name}: {score}\n")

def math_quiz():
    # Ask the user for their name
    name = input("Name: ")
    
   
    int1 = int(input("1+1=? "))
    int2 = int(input("2+2=? "))
    int3 = int(input("3+3=? "))

    score = 0
    
    print("\nResults")
    if int1 == 2:
        print("Q1 Correct")
        score += 1
    else:
        print("Q1 Incorrect")
    
    if int2 == 4:
        print("Q2 Correct")
        score += 1
    else:
        print("Q2 Incorrect")
    
    if int3 == 6:
        print("Q3 Correct")
        score += 1
    else:
        print("Q3 Incorrect")
    

