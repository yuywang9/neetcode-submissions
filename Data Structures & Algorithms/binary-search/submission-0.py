class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # left = 0 
        # right = len(nums) - 1
        # while left <= right:
        #     mid = (left + right) // 2
        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid] > target: #target on the left side
        #         right = mid - 1
        #     elif nums[mid] < target: #target on the right side
        #         left = mid + 1
        # return -1
        









        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            elif nums[m] > target:
                r = m - 1

            elif nums[m] < target:
                l = m + 1
        
        return -1
            