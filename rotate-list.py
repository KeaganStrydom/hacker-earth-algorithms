class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        shift = k % len(nums)
        shifted = nums[-shift:] # get last elements

        del nums[-shift:]

        for i in range(0, len(shifted)):
            nums.insert(i, shifted[i])