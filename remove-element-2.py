class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        filtered = [x for x in nums if (val != x)]
        k = len(filtered)
        for i in range(0, k):
            nums[i] = filtered[i]

        return len(filtered)