class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Finds the length of the longest repeating character substring after at most k replacements.
        Time Complexity: O(N). Even with the nested `while` loop, the `left` pointer only ever 
        moves forward and never resets. It traverses the string at most once. Since both `left` 
        and `right` move across the string exactly once, total operations are O(N + N) = O(N).
        Space Complexity: O(1) (at most 26 keys).
        
        The Logic:
        We use a sliding window. For a window to be valid, the number of characters we 
        MUST replace cannot exceed k.
        Formula: (Window Size) - (Count of most frequent character in window) <= k.
        
        - Expand `right` pointer and update frequency map.
        - If the formula becomes > k, the window is invalid, so shrink `left` pointer.
        - The valid window length is always `right - left`.
        """
        tracker = {}
        left = 0
        right = 0 
        max_len = 0

        while(right < len(s)):
            cur_max_len = 0
            right_char = s[right]
            tracker[right_char] = 1 + tracker.get(right_char, 0)
            right+=1

            while(right - left - max(tracker.values()) > k):
                left_char = s[left]
                tracker[left_char] -= 1
                left += 1

            cur_max_len = right-left

            if(cur_max_len > max_len):
                max_len = cur_max_len
            
        return max_len

if __name__ == '__main__':
    sol = Solution()
    print("Test 1: 'ABAB', k=2    -> Expected: 4, Got:", sol.characterReplacement("ABAB", 2))
    print("Test 2: 'AABABBA', k=1 -> Expected: 4, Got:", sol.characterReplacement("AABABBA", 1))
    print("Test 3: 'A', k=0       -> Expected: 1, Got:", sol.characterReplacement("A", 0))
    print("Test 4: 'ABAA', k=0    -> Expected: 2, Got:", sol.characterReplacement("ABAA", 0))
    print("All tests executed!")
