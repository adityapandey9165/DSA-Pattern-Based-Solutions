"""
LeetCode 1622 — Fancy Sequence
Difficulty: Hard
Topic: Design, Math, Modular Arithmetic

--------------------------------------------------

Problem
-------
Design a sequence that supports the following operations:

append(val)   → add value to sequence
addAll(inc)   → add inc to all elements
multAll(m)    → multiply all elements by m
getIndex(idx) → return element at index idx

All results are modulo 1e9+7.

--------------------------------------------------

Key Idea
--------

Instead of updating every element for each operation
(which would be O(n)), we maintain two global values:

mul → cumulative multiplication
add → cumulative addition

Any element x in the stored array represents:

actual_value = x * mul + add

When we append a new value we **reverse the operations**
so that when the global transform is applied later,
the value becomes correct.

append(val):

val = (val - add) * modular_inverse(mul)

--------------------------------------------------

Mathematics
-----------

If current transformation is:

value = x * mul + add

Then to store x:

x = (val - add) / mul

Division in modular arithmetic uses
modular inverse:

x = (val - add) * inv(mul)

--------------------------------------------------

Time Complexity
---------------

append  → O(1)
addAll  → O(1)
multAll → O(1)
getIndex→ O(1)

--------------------------------------------------

Space Complexity
----------------

O(n)

--------------------------------------------------
"""


class Fancy:

    def __init__(self):
        self.arr = []
        self.mul = 1
        self.add = 0
        self.MOD = 10**9 + 7

    def append(self, val: int) -> None:

        # modular inverse of mul
        inv = pow(self.mul, -1, self.MOD)

        val = ((val - self.add) * inv) % self.MOD

        self.arr.append(val)

    def addAll(self, inc: int) -> None:

        self.add = (self.add + inc) % self.MOD

    def multAll(self, m: int) -> None:

        self.add = (self.add * m) % self.MOD
        self.mul = (self.mul * m) % self.MOD

    def getIndex(self, idx: int) -> int:

        if idx >= len(self.arr):
            return -1

        return (self.arr[idx] * self.mul + self.add) % self.MOD


"""
Example
-------

obj = Fancy()
obj.append(2)
obj.addAll(3)
obj.append(7)
obj.multAll(2)
print(obj.getIndex(0))
"""
