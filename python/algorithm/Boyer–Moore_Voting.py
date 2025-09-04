Algorithm — Boyer–Moore Voting (one-solution explanation)

Goal: find the element that appears more than ⌊n/2⌋ times in an array nums.
Key idea: pairs of different elements cancel each other. After canceling all such pairs, the remaining element (if any) must be the majority.

Algorithm (step-by-step):

Initialize candidate = None and count = 0.

Iterate through each element x in nums:

If count == 0, set candidate = x and count = 1.

Else if x == candidate, increment count.

Else (x != candidate), decrement count.

After one pass, candidate holds the majority element (given the problem guarantee that a majority exists).

Why it works (intuition / short proof sketch):

Think of pairing each occurrence of the current candidate with a different element; each such pair reduces the "net advantage" of the candidate by 1.

If a majority element exists (> n/2 occurrences), it cannot be fully canceled by all other elements combined — after all possible cancellations, the majority remains as candidate.

(If a majority weren't guaranteed, you would need a second pass to verify candidate actually appears > n/2 times.)

Example trace:
nums = [2, 2, 1, 1, 1, 2, 2]

Start: candidate=None, count=0

See 2: count=0 → candidate=2, count=1

See 2: x==candidate → count=2

See 1: x!=candidate → count=1

See 1: x!=candidate → count=0

See 1: count==0 → candidate=1, count=1

See 2: x!=candidate → count=0

See 2: count==0 → candidate=2, count=1
Final candidate = 2 (correct)

Complexity:

Time: O(n) — single pass

Space: O(1) — only two variables

Minimal code (Boyer–Moore)
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Boyer–Moore Voting Algorithm:
        Single-pass O(n), constant space O(1).
        """
        candidate = None
        count = 0
        for x in nums:
            if count == 0:
                candidate = x
                count = 1
            elif x == candidate:
                count += 1
            else:
                count -= 1
        return candidate
