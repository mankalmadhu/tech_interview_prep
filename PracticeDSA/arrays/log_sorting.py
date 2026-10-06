class Solution:
    # @param A : list of strings
    # @return a list of strings
    # https://www.interviewbit.com/problems/reorder-data-in-log-files/
    def reorderLogs(self, A):
        """
            Reorders log files based on specific criteria.

        Types of Logs:
        1. Letter Logs: "identifier word1 word2..." (Content consists of lowercase English letters)
        2. Digit Logs: "identifier 1 2 3..." (Content consists of digits)

        Sorting Rules:
        1. Letter Logs come before Digit Logs.
        2. Letter Logs are sorted alphanumerically by CONTENT.
        3. Tie-Breaker: If contents are the same, sort by IDENTIFIER.
        4. Digit Logs maintain their original relative order (Stable).

        Strategy: Custom Sorting with Tuples
        ------------------------------------
        1. Separation: Iterate through the input and split logs into two lists:
           - 'digits': strictly for digit logs.
           - 'letters': strictly for letter logs.
        2. Sorting 'letters':
           - We need a custom key to handle the "Content -> Identifier" priority.
           - Python's sort supports tuple keys: (primary_key, secondary_key).
           - Key = (content_part, identifier_part).
        3. Merging: Return letters + digits.

        Complexity Analysis:
        --------------------
        Time Complexity: O(M * N log N)
           - N is the number of logs. M is the maximum length of a log.
           - Sorting takes N log N comparisons.
           - Each comparison involves comparing strings of length up to M.

        Space Complexity: O(M * N)
           - We store all characters of all logs in our auxiliary lists.
        """

        digit_list = []
        alpha_list = []

        def sort_key(log):
            identifier, log_start = log.split("-", 1)
            return (log_start, identifier)

        for log in A:
            log_start = log.split("-", 1)[1]
            first_char = log_start[0]

            if first_char.isalpha():
                alpha_list.append(log)

            if first_char.isdigit():
                digit_list.append(log)

        alpha_list.sort(key=sort_key)
        return alpha_list + digit_list


if __name__ == "__main__":
    A = ["dig1-8-1-5-1", "let1-art-can", "dig2-3-6", "let2-own-kit-dig", "let3-art-zero"]
    output = Solution().reorderLogs(A)
    print(output)

    import random
    import string

    def brute_force_reorder(logs):
        digit_logs = []
        letter_logs = []
        for log in logs:
            identifier, content = log.split("-", 1)
            if content[0].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append((content, identifier, log))
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
            logs.append(identifier + "-" + "-".join(words))

        got = Solution().reorderLogs(logs)
        expected = brute_force_reorder(logs)
        assert got == expected, f"Mismatch on {logs}: got {got}, expected {expected}"

    print("All stress tests passed!")
