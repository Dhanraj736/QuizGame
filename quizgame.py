class QuizGame:
    def __init__(self):
        self.questions = []
        self.correct_answers = []
        self.score = 0

    def add_question(self, question, correct_answer):
        """Add a question to the quiz with its correct answer."""
        self.questions.append(question)
        self.correct_answers.append(correct_answer.strip().lower())

    def play(self):
        """Start the quiz game and evaluate answers."""
        print("Welcome to the Quiz Game!")
        print("Let's see how much you know!\n")

        for i in range(len(self.questions)):
            print(f"Question {i + 1}: {self.questions[i]}")
            user_answer = input("Your answer: ").strip().lower()

            if user_answer == self.correct_answers[i]:
                print("Correct! Well done!\n")
                self.score += 1
            else:
                print(f"Oops! The correct answer was: {self.correct_answers[i]}\n")

        self.show_final_score()

    def show_final_score(self):
        """Display the final score after the quiz ends."""
        print("Quiz Complete!")
        print(f"Your final score is: {self.score} out of {len(self.questions)}")
        if self.score == len(self.questions):
            print("Amazing! You got a perfect score!")
        elif self.score > len(self.questions) / 2:
            print("Great job! You did well!")
        else:
            print("Keep trying! Practice makes perfect!")

# Example Usage
if __name__ == "__main__":
    quiz = QuizGame()

    # Adding questions
    quiz.add_question("What is the capital city of Italy?", "Rome")
    quiz.add_question("What is 10 x 10?", "100")
    quiz.add_question("Which language is primarily spoken in Brazil?", "Portuguese")
    quiz.add_question("Who painted the Mona Lisa?", "Leonardo da Vinci")
    quiz.add_question("Which planet is closest to the Sun?", "Mercury")

    # Starting the quiz
    quiz.play()
