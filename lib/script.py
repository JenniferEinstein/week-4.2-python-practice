import random
#from capitals import states
#print(states)

# an array of sample of state dictionaries
states = [
 {
    "name": "Maine",
    "capital": "Augusta"
}, {
    "name": "Maryland",
    "capital": "Annapolis"
}, {
    "name": "Massachusetts",
    "capital": "Boston"
}, {
    "name": "Michigan",
    "capital": "Lansing"
}, {
    "name": "Minnesota",
    "capital": "St. Paul"
}, {
    "name": "Mississippi",
    "capital": "Jackson"
}, {
    "name": "Missouri",
    "capital": "Jefferson City"
}, {
    "name": "Montana",
    "capital": "Helena"
}]


# Randomize the given state list
def shuffle_states():
    random.shuffle(states)
    return states

shuffled_states = shuffle_states()

name = input("Enter your name: ")


# ======  SCORE TRACKING VARIABLES ====== #
correct_answers = 0
incorrect_answers = 0



def ask_questions(shuffled_states):
    global correct_answers, incorrect_answers  ## allows modification of variable outside of the current scope

    for state in shuffled_states:
        question = f"What is the capital of {state['name']}? "
        student_answer = input(question)
        check_answer(student_answer, state)

def check_answer(student_answer, state):
    global correct_answers, incorrect_answers
    if student_answer.strip().lower() == state['capital'].strip().lower():
        correct_answers += 1
        print(f"Correct! The capital of {state['name']} is {state['capital']}.")
    else:
        incorrect_answers += 1
        print(f"I'm sorry. The capital of {state['name']} is {state['capital']}.")

def display_score():
    if correct_answers > 0 and incorrect_answers > 0:
        print("So far, you correctly  identified " + correct_answers + "state capitals and incorrectly identified " + incorrect_answers + " state capitals.")
    elif correct_answers > 0 and incorrect_answers == 0:
        print("So far, you have correctly identified " + correct_answers + " state capitals.")
    elif correct_answers == 0 and incorrect_answers > 0:
        print("So far, you have incorrectly identified " + incorrect_answers + " state capitals.")

display_score()

ask_questions(shuffled_states)



continuation = input("Do you want to continue? (Yes/No): ")


# =========  FUNCTIONS  ============
#  DONE  shuffle_states(): Randomize the order of states
# display_question(state): Show the current state to the user
# get_user_input(): Prompt and receive user's guess
#  DONE  check_answer(user_input, correct_capital): Verify the user's answer
# update_score(is_correct): Modify the user's score
#  DONE  display_score(): Show current or final score
# play_again(): Ask if the user wants to restart the game
