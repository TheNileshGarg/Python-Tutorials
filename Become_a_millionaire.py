# User will start from 1 and go to q no 10 
# Each time user will win an amount and we display his/ her take home money 

# List of questions
questions = [
    "What is the capital of France?",
    "Who wrote 'To Kill a Mockingbird'?",
    "What is the largest planet in our Solar System?",
    "In what year did the Titanic sink?",
    "Which element has the chemical symbol 'O'?",
    "What is the smallest prime number?",
    "Who painted the Mona Lisa?",
    "Which country is known as the Land of the Rising Sun?",
    "What is the boiling point of water in Celsius?",
    "Who is known as the father of modern physics?",
    "Which ocean is the largest by area?",
    "What is the currency of Japan?",
    "Who developed the theory of relativity?",
    "What is the largest bone in the human body?",
    "What is the main ingredient in guacamole?",
    "Which planet is known as the Red Planet?",
    "What is the hardest natural substance on Earth?",
    "Which city hosted the 2008 Summer Olympics?",
    "What is the chemical formula for water?",
    "Who wrote '1984'?"
]

# List of correct answers
correct_answers = [
    "Paris",
    "Harper Lee",
    "Jupiter",
    "1912",
    "Oxygen",
    "2",
    "Leonardo da Vinci",
    "Japan",
    "100",
    "Albert Einstein",
    "Pacific",
    "Yen",
    "Albert Einstein",
    "Femur",
    "Avocado",
    "Mars",
    "Diamond",
    "Beijing",
    "H2O",
    "George Orwell"
]
rewards = [1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000, 500000, 1000000]


# List of options for each question
options = [
    ["Paris", "London", "Berlin", "Rome"],
    ["Harper Lee", "J.K. Rowling", "Ernest Hemingway", "Mark Twain"],
    ["Earth", "Mars", "Jupiter", "Saturn"],
    ["1910", "1912", "1914", "1916"],
    ["Oxygen", "Hydrogen", "Nitrogen", "Carbon"],
    ["1", "2", "3", "5"],
    ["Leonardo da Vinci", "Vincent van Gogh", "Pablo Picasso", "Claude Monet"],
    ["Japan", "China", "South Korea", "Thailand"],
    ["90", "100", "110", "120"],
    ["Albert Einstein", "Isaac Newton", "Galileo Galilei", "Nikola Tesla"],
    ["Atlantic", "Indian", "Pacific", "Arctic"],
    ["Yuan", "Yen", "Won", "Dollar"],
    ["Albert Einstein", "Isaac Newton", "Stephen Hawking", "Niels Bohr"],
    ["Femur", "Humerus", "Tibia", "Fibula"],
    ["Avocado", "Tomato", "Cucumber", "Lettuce"],
    ["Mars", "Venus", "Mercury", "Jupiter"],
    ["Diamond", "Gold", "Silver", "Platinum"],
    ["Tokyo", "London", "Beijing", "Sydney"],
    ["H2O", "CO2", "O2", "N2"],
    ["George Orwell", "Aldous Huxley", "Ray Bradbury", "Kurt Vonnegut"]
]
def take_input():
    ui = None
    while True:
        try:
            ui = int(input("Enter an integer between 1 to 4 to chose your option. "))
            if ui in range(1,5):
                return ui 
            else:
                print("Invalid Choice. Enter an integer between 1 and 4.")
        except ValueError:
                print("Invalid Choice. Please enter a valid integer.")

import random
def random_question():
    q_no = random.randint(0,19)
    print(questions[q_no])
    print(f"Your Options are \n1.{options[q_no][0]}\n2.{options[q_no][1]}\n3.{options[q_no][2]}\n4.{options[q_no][3]}")
    inp = take_input()
    user_input_choice = options[q_no][inp - 1]
    if user_input_choice == correct_answers[q_no]:
            return True
    else:
            return False

def game():
    i = 0
    while(i < 10):
        ques = random_question()
        if(ques):
            i += 1
        else:
            break
    money = rewards[i - 1]
    print(f"Congratulations, You have won {money} dollars.")

game()      
         
