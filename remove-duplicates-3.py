class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        i = 0
        while i < len(nums):
            if (nums[i] in seen): # test whether item is seen
                nums.pop(i) # remove duplicate element
                # shift back to account for removed item
                i -= 1
            seen.add(nums[i]) # add seen item
            i += 1 # shift forward to next item
        return len(seen) 