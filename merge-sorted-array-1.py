class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        removed = 0
        i = m - 1
        j = n - 1
        while (j >= 0):
            if nums2[j] >= nums1[i]:
                nums1.insert(i + 1, nums2[j])
                nums1.pop(-1)
                j -= 1
            elif (i > 0):
                i -= 1
            else:
                nums1.insert(0, nums2[j])
                nums1.pop(-1)
                j -= 1