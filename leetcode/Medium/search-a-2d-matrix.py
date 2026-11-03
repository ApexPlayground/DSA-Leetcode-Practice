// Problem: Search a 2D Matrix
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/search-a-2d-matrix/
// Solved on: 2026-11-03T08:07:45.474Z

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

        def search(nums, target):

            l = 0
            r = len(nums) - 1

            while l <= r:
                mid = (l + r) // 2

                if nums[mid] == target:
                    return True
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return False
        
        i = 0
        j = len(matrix) - 1

        while i <= j:
            mid = (i + j) // 2

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                return search(matrix[mid], target)
            
            elif target > matrix[mid][-1]:
                i = mid + 1
            else:
                j = mid - 1
        
        return False
        
       

            

        