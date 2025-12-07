
"""
Sliding Window
Initialization:

left = 0 (the left edge of our window).

max_length = 0.

window_chars = set() (the set to store characters currently in our window).

The Loop: Iterate through the string with a right pointer from the beginning to the end. This pointer will expand the window.

Handle Duplicates: For each character s[right], check if it's already in window_chars.

If it is, you have a duplicate. You must shrink the window from the left until the old duplicate is gone. A while loop is great for this:

while s[right] in window_chars:

Remove s[left] from window_chars.

Increment left.

Expand the Window: After the while loop is done, you are guaranteed that s[right] is no longer a duplicate in the window. Now you can add the new character:

window_chars.add(s[right])

Update Max Length: The window from left to right is now a valid substring with no repeats. Calculate its length and update the max if it's bigger:

max_length = max(max_length, right - left + 1)

Return: After the for loop finishes, return max_length.

This pattern of an outer for loop to expand the window and an inner while loop to shrink it is the core of many dynamic sliding window problems. You're ready for
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