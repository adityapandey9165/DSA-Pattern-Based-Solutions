"""
LeetCode: 2092. Find All People With Secret (Hard)
Problem link: https://leetcode.com/problems/find-all-people-with-secret/
Author: Aditya Pandey
Date: 2025-12-30

Problem:
There are `n` people labeled from 0 to n-1.
Initially, person 0 and `firstPerson` know a secret.

You are given a list of meetings, where each meeting is represented as:
    [person1, person2, time]

At the given time, the two people can share the secret if one of them knows it.
People can attend multiple meetings at the same time.

Return all people who know the secret at the end.

---

Approach: Time-Based Grouping + Graph BFS

Key idea:
- Meetings happening at the same time should be processed together.
- Secret propagation is allowed **only within the same timestamp**.
- We build a graph for each timestamp and run BFS starting from
  people who already know the secret.

Steps:
1. Sort meetings by time.
2. Process meetings time-group by time-group.
3. For each time:
   - Build a temporary graph of meetings at that time.
   - Identify people involved at that time.
   - Start BFS only from people who already know the secret.
4. After BFS, update the global secret set.
5. Continue to the next timestamp.

---

Why this works:
- Prevents
