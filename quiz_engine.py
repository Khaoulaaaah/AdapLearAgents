from quiz_db import get_random_quiz, QUIZ_DB
from rag_agent import explain_misunderstood_concepts
from progress_db import init_db, log_answer, get_concept_accuracy, show_progress_summary


def ask_question(q):
    print(f"\n({q.get('difficulty', 'medium').capitalize()} question) {q['question']}")
    for i, opt in enumerate(q["options"]):
        print(f"{i+1}. {opt}")
    while True:
        ans = input("Your answer (1-4): ").strip()
        if ans in ['1', '2', '3', '4']:
            return q["options"][int(ans)-1]


def adjust_difficulty(q, correct):
    levels = ["easy", "medium", "hard"]
    current = q.get("difficulty", "medium")
    idx = levels.index(current)
    if correct and idx < 2:
        return levels[idx + 1]
    elif not correct and idx > 0:
        return levels[idx - 1]
    return current


def run_quiz(concepts, num_questions=1):
    quiz = get_random_quiz(concepts, num_questions)
    wrong_questions = []
    for concept, q in quiz:
        student_ans = ask_question(q)
        correct = student_ans == q["answer"]
        if not correct:
            print(f"❌ Incorrect. Correct answer: {q['answer']}")
            wrong_questions.append((concept, q))
        else:
            print("✅ Correct!")
        log_answer(concept, q["question"], correct)
    return wrong_questions


def get_adaptive_concepts():
    concepts = list(QUIZ_DB.keys())
    return sorted(concepts, key=lambda c: get_concept_accuracy(c))[:5]  # Focus on weakest 5


def run_learning_loop():
    init_db()
    misunderstood_questions = run_quiz(get_adaptive_concepts())

    while misunderstood_questions:
        misunderstood_concepts = list(set(concept for concept, _ in misunderstood_questions))
        print(f"\nYou misunderstood: {', '.join(misunderstood_concepts)}")

        explanations = explain_misunderstood_concepts(misunderstood_questions)
        for (concept, question) in misunderstood_questions:
            key = f"{concept}|||{question['question']}"
            explanation = explanations.get(key, "No explanation found.")
            print(f"\n📘 Explanation for {concept} - '{question['question']}':\n{explanation}")

        cont = input("\nDo you want to try again on these concepts? (yes/no): ").lower()
        if cont in ("no", "enough"):
            print("✅ Session ended.")
            show_progress_summary()
            break

        retry_concepts = list(set(concept for concept, _ in misunderstood_questions))
        misunderstood_questions = run_quiz(retry_concepts, num_questions=2)

    if not misunderstood_questions:
        print("🎉 Congratulations! You understood all concepts.")
        show_progress_summary()
