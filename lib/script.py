#from capitals import states

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
print(states)


# Request for user input
name = input("Enter your name: ")
continuation = input("Do you want to continue? (Yes/No): ")


state = "state"
question = "What is the capital of" + state + "?"
student_answer = input(question)

if student_answer.upper() == 

