class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        l = 0
        while l <= len(nums) - 3:
            if l > 0 and nums[l] == nums[l - 1]:
                l += 1
                continue
            m = l + 1
            r = len(nums) - 1
            target = -nums[l]
            while m < r:
                if m > l + 1 and nums[m] == nums[m - 1]:
                    m += 1
                    continue
                if nums[m] + nums[r] > target:
                    r -= 1
                elif nums[m] + nums[r] < target:
                    m += 1
                elif nums[m] + nums[r] == target:
                    res.append([nums[l], nums[m], nums[r]])
                    m += 1

            l += 1
        return res