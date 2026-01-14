"""
LeetCode: 1396. Design Underground System (Medium)
Problem link: https://leetcode.com/problems/design-underground-system/
Author: Aditya Pandey
Date: 2026-01-14

Problem:
Design an underground train system that supports the following operations:

1. checkIn(id, stationName, t)
   - A customer with `id` checks in at station `stationName` at time `t`.

2. checkOut(id, stationName, t)
   - The same customer checks out at station `stationName` at time `t`.

3. getAverageTime(startStation, endStation)
   - Return the average travel time between `startStation` and `endStation`.

You may assume all calls are valid and customers always check out after checking in.

---

Approach: Hash Map / Design Data Structure

We use two hash maps:

1. checkInMap:
   - Stores current check-in information.
   - Key: customer id
   - Value: (startStation, startTime)

2. routeMap:
   - Stores total travel time and trip count for each route.
   - Key: (startStation, endStation)
   - Value: [totalTime, tripCount]

Steps:
- On checkIn:
  - Store the user's start station and time.
- On checkOut:
  - Retrieve and remove check-in info.
  - Update total travel time and count for that route.
- On getAverageTime:
  - Return totalTime / tripCount.

---

Time Complexity:
- checkIn: O(1)
- checkOut: O(1)
- getAverageTime: O(1)

Space Complexity:
- O(n), where n is number of active check-ins and routes
"""


class UndergroundSystem:

    def __init__(self):
        # id -> (startStation, startTime)
        self.check_in = {}

        # (startStation, endStation) -> [totalTime, tripCount]
        self.routes = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.check_in.pop(id)
        key = (start_station, stationName)

        if key not in self.routes:
            self.routes[key] = [0, 0]

        self.routes[key][0] += (t - start_time)
        self.routes[key][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time, count = self.routes[(startStation, endStation)]
        return total_time / count


# -----------------------
# Quick tests for local verification
# -----------------------
if __name__ == "__main__":
    undergroundSystem = UndergroundSystem()

    undergroundSystem.checkIn(45, "Leyton", 3)
    undergroundSystem.checkIn(32, "Paradise", 8)
    undergroundSystem.checkIn(27, "Leyton", 10)

    undergroundSystem.checkOut(45, "Waterloo", 15)
    undergroundSystem.checkOut(27, "Waterloo", 20)
    undergroundSystem.checkOut(32, "Cambridge", 22)

    print(undergroundSystem.getAverageTime("Leyton", "Waterloo"))
    # Expected: 11.0

    undergroundSystem.checkIn(10, "Leyton", 24)
    undergroundSystem.checkOut(10, "Waterloo", 38)

    print(undergroundSystem.getAverageTime("Leyton", "Waterloo"))
    # Expected: 12.0
