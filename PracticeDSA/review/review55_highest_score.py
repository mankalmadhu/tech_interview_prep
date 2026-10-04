"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/math/highest_score.py until you're done.

Problem (Highest Score, InterviewBit):

https://www.interviewbit.com/problems/highest-score/

Given a 2D list A where each row is [student_id, score], each
student may appear multiple times (multiple scores recorded).
Compute each student's AVERAGE score, and return the highest
average score among all students (as an int, floor/truncated).

Example:
  A = [["a", "1"], ["b", "2"], ["a", "3"]]
  student a: scores [1, 3] -> avg 2.0
  student b: scores [2]    -> avg 2.0
  output = 2

Write your solution below.
"""


def highest_score(A):
    scores = {}

    for marks in A:
        student = marks[0]
        score = int(marks[1])

        cur_scores = scores.get(student,[])
        cur_scores.append(score)
        scores[student] = cur_scores


    # Calculate averages
    averages = []
    for score in scores.values():
        avg = sum(score) / len(score)
        averages.append(avg)


    # Return the highest average
    return int(max(averages))



def brute_force_highest(A):
    student_scores = {}
    for student, score in A:
        student_scores.setdefault(student, []).append(int(score))
    best = None
    for scores in student_scores.values():
        avg = sum(scores) / len(scores)
        if best is None or avg > best:
            best = avg
    return int(best)


if __name__ == "__main__":
    print(highest_score([["a", "1"], ["b", "2"], ["a", "3"]]))  # expect 2
    print(highest_score([["a", "10"], ["a", "20"], ["b", "5"]]))  # expect 15
    print(highest_score([["x", "7"]]))  # expect 7

    import random
    import string

    for trial in range(300):
        num_students = random.randint(1, 10)
        students = list(string.ascii_lowercase[:num_students])
        A = []
        for _ in range(random.randint(1, 50)):
            student = random.choice(students)
            score = random.randint(0, 100)
            A.append([student, str(score)])

        got = highest_score(A)
        expected = brute_force_highest(A)
        assert got == expected, f"Mismatch on {A}: got {got}, expected {expected}"

    print("All stress tests passed!")
