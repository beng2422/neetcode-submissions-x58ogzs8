class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2[:n]
        nums1.sort()

        # for i in range(len(nums2)):
        #     if nums2[0]<=nums1[0]:
        #         nums1 = [nums2[0]] + nums1
        #         nums1 = nums1[:len(nums1)-1]
        #         nums2=nums2[1:]
        # for i in range(1, len(nums1)):
        #     print(nums1)
        #     if not nums2:
        #         break
        #     if nums1[i-1]<=nums2[0] <=nums1[i]:
        #         nums1 = nums1[:i] + [nums2[0]] + nums1[i:]
        #         nums2=nums2[1:]
        #         nums1 = nums1[:len(nums1)-1]
