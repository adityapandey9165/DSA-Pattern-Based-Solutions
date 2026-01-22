"""
LeetCode: 316. Remove Duplicate Letters (Medium)
Problem Link: https://leetcode.com/problems/remove-duplicate-letters/
Author: Aditya Pandey
Date: 2026-01-19

--------------------------------------------------
Problem:
Given a string `p`, remove duplicate letters so that:
1. Every letter appears exactly once
2. The resulting string is the smallest in lexicographical order
   among all possible results.

--------------------------------------------------
Pattern:
Monotonic Stack + Greedy + Frequency Count

--------------------------------------------------
Core Idea:
We want:
- Each character only once
- Lexicographically smallest result

This is achieved by:
- Using a stack to maintain increasing lexicographical order
- Removing previously added characters if:
  - They are greater than the current character
  - They appear again later in the string

--------------------------------------------------
Approach:
1. Count the frequency of each character.
2. Iterate through the string:
   - Decrease frequency of current character
   - If character is already used, skip it
3. While:
   - Stack is not empty
   - Current character is smaller than top of stack
   - Top of stack appears later again (frequency > 0)
   → Pop from stack and mark it unused
4. Push current character to stack
5. Join stack to form result

--------------------------------------------------
Why This Works:
- Stack ensures lexicographical order
- Frequency check ensures we don't lose characters permanently
- Greedy removal guarantees smallest possible sequence

--------------------------------------------------
Example:
Input: "cbacdcbc"

Step-by-step:
Stack evolution:
c → b → a → ac → acd → acdb

Output:
"acdb"

--------------------------------------------------
Time Complexity:
O(n)

Space Complexity:
O(n)

--------------------------------------------------
Things to Pay Attention:
- Frequency decrement before comparison
- Do not remove characters that won't appear again
- Stack must remain lexicographically minimal
--------------------------------------------------
"""

from collections import defaultdict


class Solution:
    def removeDuplicateLetters(self, p: str) -> str:
        stack = []
        seen = set()
        freq = defaultdict(int)

        # Count frequency
        for ch in p:
            freq[ch] += 1

        for ch in p:
            freq[ch] -= 1

            # Skip if already used
            if ch in seen:
                continue

            # Maintain lexicographical order
            while stack and ch < stack[-1] and freq[stack[-1]] > 0:
                seen.remove(stack.pop())

            stack.append(ch)
            seen.add(ch)

        return "".join(stack)


# -----------------------
# Local Testing
# -----------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.removeDuplicateLetters("bcabc"))      # Expected: "abc"
    print(sol.removeDuplicateLetters("cbacdcbc"))   # Expected: "acdb"
