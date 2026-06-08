import random
questions = {
    "what is Python": "peogramming language",
    "how work python? " : "this is a projects",
    "what is your name": "Nare",
    "how are old you": "21",
    "where are you from": "from armenia",
    "what is your male": "famale"
}
def python_trivial_game():
    question_list = list(questions.keys())
    total_question = 2
    score = 0

    slected_question = random.sample(question_list, total_question)

    for idx, questions in enumerate(slected_question):
        print(f"{idx +1} ,{questions}")
   
python_trivial_game()