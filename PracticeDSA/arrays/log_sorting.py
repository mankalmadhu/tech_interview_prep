class Solution:
    # @param A : list of strings
    # @return a list of strings
    # https://www.interviewbit.com/problems/reorder-data-in-log-files/
    def reorderLogs(self, A):

        digit_list = []
        alpha_list = []

        def sort_key(log):
            identifier, log_start = log.split('-', 1)
            return (log_start, identifier)

        for log in A:
            log_start = log.split('-', 1)[1]
            first_char = log_start[0]

            if first_char.isalpha():
                alpha_list.append(log)

            if first_char.isdigit():
                digit_list.append(log)

        alpha_list.sort(key=sort_key)
        return alpha_list + digit_list


A = [
    "dig1-8-1-5-1", "let1-art-can", "dig2-3-6", "let2-own-kit-dig",
    "let3-art-zero"
]
output = Solution().reorderLogs(A)
print(output)
