from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total_time = 0

        for point in range(0, len(points) - 1):
            x1, y1 = points[point]
            x2, y2 = points[point + 1]

            time_taken = max(abs(x2-x1), abs(y2 - y1))
            total_time += time_taken
        
        return total_time


s = Solution()

print(s.minTimeToVisitAllPoints([[3,2],[-2,2]]))