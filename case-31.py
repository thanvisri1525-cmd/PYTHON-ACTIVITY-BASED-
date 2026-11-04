print("EXAMINATION ANSWER EVALUATION")

answer_key = ["A", "B", "C", "D", "A"]
student_answers = []

for i in range(5):
    answer = input(
        f"Enter answer for question {i + 1}: "
    ).strip().upper()

    if answer not in ["A", "B", "C", "D"]:
        print("Invalid answer. Use A, B, C, or D.")
        break

    student_answers.append(answer)

if len(student_answers) == 5:
    correct = 0

    for i in range(5):
        if student_answers[i] == answer_key[i]:
            correct += 1

    incorrect = 5 - correct
    score = correct

    print("Correct answers:", correct)
    print("Incorrect answers:", incorrect)
    print("Final score:", score, "/ 5")
