"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/arrays/log_sorting.py until you're done.

Problem (Reorder Data in Log Files):

https://www.interviewbit.com/problems/reorder-data-in-log-files/

Each log is a string of the form "identifier word1 word2 ...".
There are two kinds of logs:
  - Letter logs: identifier followed by only lowercase letters.
  - Digit logs: identifier followed by only digits.

Reorder the logs so that:
  1. Letter logs come before all digit logs.
  2. Letter logs are sorted lexicographically by their content
     (the part after the identifier); ties broken by identifier.
  3. Digit logs stay in their original input order.

Example:
  logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6",
          "let2 own kit dig", "let3 art zero"]
  output = ["let1 art can", "let3 art zero", "let2 own kit dig",
            "dig1 8 1 5 1", "dig2 3 6"]

Write your solution below.
"""


def reorder_logs(logs):
    digits = []
    alphabects = []
    delimiter = " "

    def sorter(log):
        identifier, log_start = log.split(delimiter, 1)
        return (log_start, identifier)

    for log in logs:
        log_start = log.split(delimiter, 1)[1]
        char = log_start[0]

        if char.isalpha():
            alphabects.append(log)

        if char.isdigit():
            digits.append(log)

    alphabects.sort(key=sorter)
    return alphabects + digits



if __name__ == "__main__":
    logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6",
            "let2 own kit dig", "let3 art zero"]
    print(reorder_logs(logs))
    # expect ["let1 art can", "let3 art zero", "let2 own kit dig",
    #         "dig1 8 1 5 1", "dig2 3 6"]

    import random
    import string

    def brute_force_reorder(logs):
        digit_logs = []
        letter_logs = []
        for log in logs:
            identifier, content = log.split(" ", 1)
            if content[0].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append((content, identifier, log))
        # stable sort by (content, identifier) - independent manual sort key
        letter_logs.sort(key=lambda t: (t[0], t[1]))
        return [t[2] for t in letter_logs] + digit_logs

    for trial in range(300):
        n = random.randint(0, 20)
        logs = []
        for i in range(n):
            identifier = f"id{i}"
            if random.random() < 0.5:
                words = [
                    "".join(random.choices(string.ascii_lowercase, k=random.randint(1, 5)))
                    for _ in range(random.randint(1, 3))
                ]
            else:
                words = [str(random.randint(0, 9)) for _ in range(random.randint(1, 3))]
            logs.append(identifier + " " + " ".join(words))

        got = reorder_logs(logs)
        expected = brute_force_reorder(logs)
        assert got == expected, f"Mismatch on {logs}: got {got}, expected {expected}"

    print("All stress tests passed!")
