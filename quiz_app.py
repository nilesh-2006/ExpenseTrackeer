import json
import time
import os

# ------------------ Load Questions from JSON ------------------
def load_questions():
    try:
        with open("questions.json", "r") as file:
            return json.load(file)
    except:
        print("Error: questions.json not found!")
        exit()

# ------------------ Save Score to JSON file ------------------
def save_score(username, score, total):
    score_data = {
        "username": username,
        "score": score,
        "total": total,
        "time": time.ctime()
    }

    # If file doesn't exist, create it
    if not os.path.exists("scores.json"):
        with open("scores.json", "w") as file:
            json.dump([score_data], file, indent=4)
    else:
        # Append score to existing file
        with open("scores.json", "r") as file:
            data = json.load(file)

        data.append(score_data)

        with open("scores.json", "w") as file:
            json.dump(data, file, indent=4)

# ------------------ Quiz Logic ------------------
def start_quiz(username):
    questions = load_questions()
    total = len(questions)
    score = 0

    print("\n************* QUIZ STARTED *************")

    for q in questions:
        print("\n" + q["question"])
        for opt in q["options"]:
            print(opt)

        # Timer: 10 seconds per question
        print("⏳ You have 10 seconds to answer...")
        start_time = time.time()

        answer = ""
        while True:
            if time.time() - start_time > 10:
                print("⏰ Time Up! Moving to next question.")
                answer = ""
                break
            if answer == "":
                answer = input("Enter answer (A/B/C/D): ").upper()

            # If user entered a value
            if answer != "":
                break

        # Check answer
        if answer == q["answer"]:
            print("✔ Correct!")
            score += 1
        else:
            print("✘ Wrong! Correct answer:", q["answer"])

    # ---------------- Final Result ----------------
    print("\n************* QUIZ COMPLETED *************")
    print("Your Score:", score, "/", total)

    # Save the score
    save_score(username, score, total)
    print("Score saved successfully!")

    # Final message
    if score == total:
        print("🔥 Excellent! Full marks!")
    elif score >= total // 2:
        print("🙂 Good job!")
    else:
        print("😢 Better luck next time!")

# ------------------ Multiple Attempts Allow ------------------
if __name__ == "__main__":
    print("===== Welcome to the Advanced Quiz App =====")
    user = input("Enter your name: ")

    while True:
        start_quiz(user)

        choice = input("\nDo you want to play again? (yes/no): ").lower()
        if choice != "yes":
            print("Thanks for playing!")
            break
