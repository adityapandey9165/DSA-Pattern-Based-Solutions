"""
LeetCode: 380. Insert Delete GetRandom O(1) (Medium)
Problem link: https://leetcode.com/problems/insert-delete-getrandom-o1/
Author: Aditya Pandey
Date: 2025-09-08

Problem:
Design a data structure that supports all following operations in average O(1) time.

1. insert(val): Inserts an item val into the set if not present. Returns True if the item was not present, False otherwise.
2. remove(val): Removes an item val from the set if present. Returns True if the item was present, False otherwise.
3. getRandom(): Returns a random element from the current set of elements. Each element must have the same probability of being returned.

Notes:
- Elements are unique (it's a set) — you don't have to handle duplicates for this problem.
- getRandom should run in O(1) time and return a uniformly random element.

Why a naive set won't cut it:
- Python's built-in set supports O(1) insert/remove, but it does NOT support O(1) random access by index.
- Converting the set to a list for every getRandom() call makes getRandom O(n).

-----------------------------------------------------------
Approach (the classic and interview-expected solution)
-----------------------------------------------------------
Use two data structures together:

1) A list `arr` that stores the values. This gives O(1) random access (random.choice or indexing).
2) A dictionary `pos` mapping value -> index in `arr`. This gives O(1) membership check and index lookup.

Insertion:
- If value is already in `pos`, return False.
- Append value to `arr`, set pos[val] = len(arr)-1, return True.

Removal (the trickiest part):
- If value not in `pos`, return False.
- Let idx = pos[val], last = arr[-1].
- Move last into arr[idx] (overwrite), update pos[last] = idx.
- Pop the last element from arr (O(1)).
- del pos[val].
- Return True.

This swap-to-end strategy avoids O(n) removal from the middle of a list.

getRandom:
- Use random.choice(arr) (O(1)) — make sure arr is not empty before calling.

Complexities:
- insert: average O(1)
- remove: average O(1)
- getRandom: O(1)
- space: O(n)

-----------------------------------------------------------
Implementation
-----------------------------------------------------------
"""
import random
from typing import Optional

class RandomizedSet:
    def __init__(self):
        # list of values
        self.arr = []        # type: list[int]
        # map value -> index in arr
        self.pos = {}        # type: dict[int, int]

    def insert(self, val: int) -> bool:
        """Inserts val if not present. Returns True if inserted, False if already present."""
        if val in self.pos:
            return False
        self.pos[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        """Removes val if present. Returns True if removed, False if not present."""
        if val not in self.pos:
            return False

        idx = self.pos[val]
        last = self.arr[-1]

        # Move last element to the place idx (only if val is not last itself)
        self.arr[idx] = last
        self.pos[last] = idx

        # Remove last element and delete mapping for val
        self.arr.pop()
        del self.pos[val]
        return True

    def getRandom(self) -> Optional[int]:
        """Returns a random element. Returns None if empty (you can choose to raise instead)."""
        if not self.arr:
            return None
        return random.choice(self.arr)

# -------------------------
# Quick tests & example trace
# -------------------------
if __name__ == "__main__":
    rs = RandomizedSet()

    # Example sequence (expected behavior shown in comments)
    print(rs.insert(1))   # True  (insert 1)
    print(rs.remove(2))   # False (2 not present)
    print(rs.insert(2))   # True  (insert 2)
    # Now arr could be [1,2], pos={1:0, 2:1}
    print(rs.getRandom() in {1,2})  # True (randomly 1 or 2)
    print(rs.remove(1))   # True  (remove 1)
    # After removal, arr becomes [2], pos={2:0}
    print(rs.insert(2))   # False (2 already present)

    # More tests
    rs2 = RandomizedSet()
    assert rs2.insert(10) is True
    assert rs2.insert(20) is True
    assert rs2.insert(30) is True
    assert rs2.remove(20) is True
    assert 20 not in rs2.pos
    assert len(rs2.arr) == 2
    # getRandom returns either 10 or 30
    val = rs2.getRandom()
    assert val in (10, 30)

    print("All quick checks passed.")

# -------------------------
# Interview talking points & common follow-ups
# -------------------------
"""
Common interview prompts / follow-ups derived from this problem:

1) Allow duplicates: How would you support duplicates while keeping operations near O(1)?
   - Use a dict mapping value -> set/list of indices. Removal becomes slightly more complex: pick one stored index for that value, swap with last, update indices for moved element, and update the index set for the removed value.

2) getRandomWeighted(): return a random element with weights. How to support O(log n) or O(1) weighted sampling?
   - Prefix-sum + binary search (O(log n) for sampling); alias method for O(1) sampling after O(n) preprocessing.

3) getRandomK(k): return k distinct random elements from the set.
   - If k << n, do repeated random picks with a hash to avoid duplicates. For k close to n, shuffle the list (Fisher–Yates) and take first k.

4) Thread-safety / concurrent access: how to make it safe under concurrency?
   - Add locks around operations or use concurrent data structures. Discuss performance tradeoffs.

5) Memory / persistence constraints: store on disk or in a database.
   - Map+array can be serialized; discuss tradeoffs and how to keep indexes consistent.

6) What if remove should return the removed value or raise on empty getRandom?
   - Choose a consistent API (raise exception or return None) and document it.

7) Edge cases & pitfalls interviewers expect you to cover:
   - Removing the last element (val == last) — the swap still works; make sure updating pos[last] doesn't clobber the entry before deletion.
   - Calling getRandom on an empty set (decide whether to raise or return None).
   - Using random.choice on an empty list raises IndexError; guard for empty case if your API expects None instead.

"""

# -------------------------
# Short note: What to explain in an interview
# -------------------------
"""
In interviews, explain clearly:
1. Why a single hashset isn't enough (no O(1) random access).
2. The two-structure design (list + map) and how they complement each other.
3. The swap trick for O(1) removal from the list.
4. Complexity analysis and edge cases (e.g., empty set, val==last).
5. Follow-ups you can handle: duplicates, weighted sampling, getRandomK, concurrency.

If you implement in Python, mention random.choice on a list is O(1) and len(list) is O(1).

Good luck — add this file to your repo and use the comment block at the top as the README for this problem.
"""
