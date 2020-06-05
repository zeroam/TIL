"""random_quiz_generator.py
creates quizzes with questions and answers in random order, along with the answer key"""
import random

# The quiz data. Keys are state and values are their capitals
capitals = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Connecticut": "Hartford",
    "Delaware": "Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    "Hawaii": "Honolulu",
    "Idaho": "Boise",
    "Illinois": "Springfield",
    "Indiana": "Indianapolis",
    "Iowa": "Des Moines",
    "Kansas": "Topeka",
    "Kentucky": "Frankfort",
    "Louisiana": "Baton Rouge",
    "Maine": "Augusta",
    "Maryland": "Annapolis",
    "Massachusetts": "Boston",
    "Michigan": "Lansing",
    "Minnesota": "Saint Paul",
    "Mississippi": "Jackson",
    "Missouri": "Jefferson City",
    "Montana": "Helena",
    "Nebraska": "Lincoln",
    "Nevada": "Carson City",
    "New Hampshire": "Concord",
    "New Jersey": "Trenton",
    "New Mexico": "Santa Fe",
    "New York": "Albany",
    "North Carolina": "Raleigh",
    "North Dakota": "Bismarck",
    "Ohio": "Columbus",
    "Oklahoma": "Oklahoma City",
    "Oregon": "Salem",
    "Pennsylvania": "Harrisburg",
    "Rhode Island": "Providence",
    "South Carolina": "Columbia",
    "South Dakota": "Pierre",
    "Tennessee": "Nashville",
    "Texas": "Austin",
    "Utah": "Salt Lake City",
    "Vermont": "Montpelier",
    "Virginia": "Richmond",
    "Washington": "Olympia",
    "West Virginia": "Charleston",
    "Wisconsin": "Madison",
    "Wyoming": "Cheyenne",
}

# Generate 35 quiz files
for quiz_num in range(35):
    # Create the quiz and answer key files
    quiz_file = open(f"capitalquiz{quiz_num + 1}.txt", "w")
    answer_key_file = open(f"capitalquiz_answers{quiz_num + 1}.txt", "w")

    # Write the header for the quiz
    quiz_file.write("Name:\n\nDate:\n\n:Period:\n\n")
    quiz_file.write(("" * 20) + f"State Capitals Quiz(Form{quiz_num + 1}")
    quiz_file.write("\n\n")

    # Shuffle the order of the states
    states = list(capitals.keys())
    random.shuffle(states)

    # Loop through all 50 states, making a question for each
    for question_num in range(50):
        # Get right and wrong answers
        correct_answers = capitals[states[question_num]]
        wrong_answers = list(capitals.values())
        del wrong_answers[wrong_answers.index(correct_answers)]
        wrong_answers = random.sample(wrong_answers, 3)
        answer_options = wrong_answers + [correct_answers]
        random.shuffle(answer_options)

        # Write the question and answer optinos to the quiz file
        quiz_file.write(
            f"{question_num + 1}. What is the capital of {states[question_num]}?\n"
        )
        for i in range(4):
            quiz_file.write(f"    {'ABCE'[i]}. {answer_options[i]}\n")
        quiz_file.write("\n")

        # Write the answer key to a file
        answer_key_file.write(f"{question_num + 1}. {'ABCD'[answer_options.index(correct_answers)]}")

    quiz_file.close()
    answer_key_file.close()
