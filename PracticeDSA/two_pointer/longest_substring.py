
"""
Finds the length of the longest substring without repeating characters.

        Strategy: Sliding Window + Set
        ------------------------------
        1. Maintain a 'window' [start, end] of unique characters.
        2. Use a Set to track characters currently in the window for O(1) lookups.
        3. Expand 'end' pointer:
           - If s[end] is NOT in set: Add it, update max_len.
           - If s[end] IS in set: We have a duplicate.
             - Increment 'start' and remove s[start] from the set until the 
               duplicate character is removed.
             - Then add s[end] and continue.

        Complexity Analysis:
        --------------------
        Time Complexity: O(N)
           - 'end' pointer moves 0 -> N.
           - 'start' pointer moves 0 -> N.
           - Each character is added once and removed at most once. Total ~2N operations.
        
        Space Complexity: O(min(N, A))
           - The set stores unique characters. In the worst case, it stores all 
             distinct characters in the alphabet 'A' (or N if N < A).
"""
def longest_substring_lenth(s):
    left = 0
    max_length = 0
    window_chars = set()

    for right in range(len(s)):
        while s[right] in window_chars:
            window_chars.remove(s[left])
            left += 1
    
        window_chars.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length