"""
LeetCode: 215. Kth Largest Element in an Array (Medium)
Problem link: https://leetcode.com/problems/kth-largest-element-in-an-array/
Author: Aditya Pandey
Date: 2025-09-08

Problem:
Given an integer array nums and an integer k, return the kth largest element in the array.

Note: It is the kth largest element in sorted order, not the kth distinct element.

---

Approach 1: Min-Heap (heapq)
- Maintain a min-heap of size k.
- Iterate through elements, pushing into heap.
- If heap grows beyond size k, pop the smallest.
- After processing all numbers, the root of the heap = kth largest.
- Time: O(n log k)
- Space: O(k)

Approach 2: Quickselect (based on QuickSort partitioning)
- Idea: Partition array around a pivot, placing all smaller/equal values to left, larger to right.
- Depending on pivot index:
    - If pivot == target index → answer found.
    - If pivot < target → search right partition.
    - If pivot > target → search left partition.
- Average Time: O(n), Worst-case: O(n^2) (if pivot choices are bad).
- Space: O(1) (in-place).

Pattern:
- Heap → useful when k is small compared to n.
- Quickselect → better for average-case efficiency (expected O(n)).

Common Interview Questions:
1. Difference between sorting, heap, and quickselect approaches?
   - Sorting: O(n log n), simplest.
   - Heap: O(n log k), good if k is small.
   - Quickselect: O(n) average, optimal for one-time query.
2. What if multiple queries for different k? (Use heap or sort once).
3. What if array is streaming / too large? (Heap is preferred).
4. Can you implement max-heap manually without Python's `heapq` (which is min-heap)?
5. How do you handle duplicates? (Doesn't matter, we just care about kth index).

Example:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Explanation: Sorted array = [1,2,3,4,5,6], 2nd largest = 5
"""

from typing import List
import heapq

# --- Approach 1: Min-Heap ---
class SolutionHeap:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return min_heap[0]


# --- Approach 2: Quickselect ---
class SolutionQuickSelect:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target_index = len(nums) - k  # Convert kth largest → kth smallest index

        def quickSelect(l, r):
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]  # place pivot at correct pos

            if p < target_index:
                return quickSelect(p + 1, r)
            elif p > target_index:
                return quickSelect(l, p - 1)
            else:
                return nums[p]

        return quickSelect(0, len(nums) - 1)
