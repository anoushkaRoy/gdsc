# main.py

from quiz import Quiz

def main():
    quiz = Quiz()
    quiz.shuffle_questions()
    
    while quiz.do_questions_remain():
        question_text = quiz.next_question()
        print(question_text)
        user_answer = input("Enter True or False: ").strip().lower()
        
        if user_answer == 'true':
            user_answer = True
        elif user_answer == 'false':
            user_answer = False
        else:
            print("Invalid input. Please enter 'True' or 'False'.")
            continue
        
        quiz.check_answer(user_answer)

    print("Quiz completed!")
    print("Your final score is:", quiz.get_score())

if __name__ == "__main__":
    main()
