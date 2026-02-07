"""
LeetCode: 1653. Minimum Deletions to Make String Balanced (Easy)
Problem Link: https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/
Author: Aditya Pandey
Date: 2026-02-07

------------------------------------------------------------
Problem:
You are given a string s consisting only of 'a' and 'b'.

A string is balanced if there is no index i < j such that:
    s[i] == 'b' and s[j] == 'a'

In other words, all 'a' characters must appear before all 'b' characters.

Return the minimum number of deletions needed to make the string balanced.

------------------------------------------------------------
Pattern:
Greedy + Prefix Counting
(Sliding decision over split positions)

------------------------------------------------------------
Key Idea:
Think of choosing a "cut" in the string.
- On the LEFT side, we want only 'a' → delete all 'b'
- On the RIGHT side, we want only 'b' → delete all 'a'

For every possible cut:
    deletions = (# of 'b' on the left) + (# of 'a' on the right)

We efficiently compute this using a single pass.

------------------------------------------------------------
Optimal Approach (Greedy / One Pass):

1. Count total number of 'a' in the string → na
2. Traverse from left to right:
   - a_count = number of 'a' seen so far
   - b_count = number of 'b' seen so far
3. At each position, compute:
       deletions = (na - a_count) + b_count
4. Track the minimum deletions

------------------------------------------------------------
Why this works:
- Every valid balanced string corresponds to some cut position
- We check all possible cuts implicitly in O(n)
- No backtracking or extra arrays needed

------------------------------------------------------------
Alternative Approaches:
1. Brute Force:
   - Try all split points
   - Count deletions for each
   - Time: O(n²) → TLE for large inputs

2. Prefix + Suffix Arrays:
   - Precompute prefix b-counts and suffix a-counts
   - Time: O(n), Space: O(n)
   - Works, but unnecessary extra space

3. Greedy (This Solution) ✅
   - Time: O(n)
   - Space: O(1)
   - Best and interview-preferred

------------------------------------------------------------
Time Complexity: O(n)
Space Complexity: O(1)

------------------------------------------------------------
Common Mistakes:
- Forgetting to count deletions AFTER updating prefix counts
- Off-by-one errors in split logic
- Using brute force for large strings
- Not handling all-'a' or all-'b' cases

------------------------------------------------------------
"""

class Solution:
    def minimumDeletions(self, s: str) -> int:
        # total number of 'a' in the string
        na = s.count("a")

        a_count = 0   # 'a' seen so far
        b_count = 0   # 'b' seen so far
        res = len(s)  # worst case: delete all characters

        for ch in s:
            if ch == "a":
                a_count += 1

            # deletions needed if we cut after this character
            res = min(res, (na - a_count) + b_count)

            if ch == "b":
                b_count += 1

        return res


# -----------------------
# Local Testing
# -----------------------
if __name__ == "__main__":
    sol = Solution()

    tests = [
        ("aababb", 2),
        ("bbaaaaabb", 2),
        ("bbbb", 0),
        ("aaaa", 0),
        ("abababab", 4),
        ("ba", 1),
        ("ab", 0),
    ]

    for s, expected in tests:
        print(f"{s} -> {sol.minimumDeletions(s)} (Expected: {expected})")
