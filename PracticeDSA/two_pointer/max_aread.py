
"""
The Logic
Let's say our left pointer is at a height of 3 and our right pointer is at a height of 8. The width is, say, 7.

height[left] = 3

height[right] = 8

The current area is min(3, 8) * 7 = 3 * 7 = 21.

The area is constrained by the shorter line (height 3).

If we move the taller pointer (the '8') inward: The best-case scenario is that we find a new line that is even taller, say 10. The new area would be min(3, 10) * 6 = 3 * 6 = 18. The area got smaller. The limiting factor is still the '3', and the width decreased, so there was no possibility of finding a larger area.

If we move the shorter pointer (the '3') inward: We lose the current limiting line. We have a chance of finding a new line that is taller, say 6. The new area would be min(6, 8) * 6 = 6 * 6 = 36. We found a larger area!

By moving the pointer of the shorter line, we get rid of the element that is limiting our area and create a chance to find a better one.
"""
def calculate_max_area(height):
    left = 0
    right = len(height) -1

    max_area = 0

    while left < right:
        current_area = (right-left) * min(height[right], height[left])
        if current_area > max_area:
            max_area = current_area
        
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area
        