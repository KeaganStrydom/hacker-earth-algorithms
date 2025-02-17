class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        for i in range(0, m):
            for j in range(0, len(nums2) - 1):
                if nums2[j] < nums1[i]:
                    # Pop and insert
                    nums1.insert(nums2[j], i)
                    nums1.pop(-1) # Delete last element
                    nums2.pop(0)
                    
        for i in range(0, len(nums2)):
            removed = n - len(nums2)
            nums1[i + m + removed] = nums2[i]
