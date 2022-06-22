
import random
from string import ascii_lowercase
import pathlib
try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib


NUM_QUESTIONS_PER_QUIZ = 5
QUESTIONS_PATH = pathlib.Path(__file__).parent / "questions.toml"
QUESTIONS = tomllib.loads(QUESTIONS_PATH.read_text())

def run_quiz():
    questions = prepare_questions(QUESTIONS, NUM_QUESTIONS_PER_QUIZ)

    num_correct = 0
    for num, (question, alternatives) in enumerate(questions, 1):
        print(f"\nQuestion {num}:")
        num_correct += ask_question(question, alternatives)

    print(f"\nYou got {num_correct} correct answers out of {num} questions")

def prepare_questions(questions, num_questions):
    num_quiz_questions = min(num_questions, len(questions))
    return random.sample(list(QUESTIONS.items()), k= num_quiz_questions)

def ask_question(question, alternatives):
    correct_answer = alternatives[0]
    ordered_alternatives = random.sample(alternatives, k=len(alternatives))

    answer = get_answer(question, ordered_alternatives)
    if answer == correct_answer:
        print("⭐ Correct! ⭐")
        return 1
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")
        return 0

def get_answer(question, alternatives):
    print(f"{question}?")
    labeled_alternatives = dict(zip(ascii_lowercase, alternatives))
    for label, alternative in labeled_alternatives.items():
        print(f"{label}) {alternative}")

    while (answer_label := input("\nChoice? ")) not in labeled_alternatives:
        print(f"Please enter one of {','.join(labeled_alternatives)}")

    return labeled_alternatives[answer_label]


if __name__ == "__main__":
    run_quiz()