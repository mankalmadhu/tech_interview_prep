# https://www.interviewbit.com/problems/highest-score/
class Solution:
    def highestScore(self, A):
        student_scores = {}

        for marks in A:
            student = marks[0]
            score = int(marks[1])

            if student in student_scores:
                student_scores[student].append(score)
            else:
                student_scores[student] = [score]

        # Calculate averages
        averages = []
        for scores in student_scores.values():
            avg = sum(scores) / len(scores)
            averages.append(avg)

        # Return the highest average
        return int(max(averages))


def _brute_force_highest(A):
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
    sol = Solution()
    print(sol.highestScore([["a", "1"], ["b", "2"], ["a", "3"]]))  # expect 2
    print(sol.highestScore([["a", "10"], ["a", "20"], ["b", "5"]]))  # expect 15
    print(sol.highestScore([["x", "7"]]))  # expect 7

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

        sol = Solution()
        got = sol.highestScore(A)
        expected = _brute_force_highest(A)
        assert got == expected, f"Mismatch on {A}: got {got}, expected {expected}"

    print("All stress tests passed!")
