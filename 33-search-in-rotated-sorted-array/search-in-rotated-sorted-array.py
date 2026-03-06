
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        size = len(nums)
        start = 0
        end = size - 1

        while start <= end:
            mid = start + (end-start) // 2

            if nums[mid] == target:
                return mid

            if nums[start] <= nums[mid]:
                # means this part is sorted in array
                if target >= nums[start] and target <= nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if target >= nums[mid] and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1

        return -1 