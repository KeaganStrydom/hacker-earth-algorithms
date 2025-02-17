class Solution:
    def majorityElement(self, nums: List[int]) -> int:
            counter = {}
            for num in nums:
                if num in counter:
                    counter[num] += 1
                else:
                    counter[num] = 1
            
            max_count = -1
            ans = -1

            for key, val in counter.items():
                if val > max_count:
                    max_count = val
                    ans = key
            
            return ans


# Better O(n) Space O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = -1
        count = 0

        for num in nums:
            if count == 0:
                ans = num
            
            if (num == ans):
                count += 1
            else:
                count -= 1
        return ans