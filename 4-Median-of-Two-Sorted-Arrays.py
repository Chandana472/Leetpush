class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        combined = nums1 + nums2
        combined.sort()
        n = len(combined)
        if n%2 == 0:
            median = (combined[n // 2 - 1] + combined[n // 2]) / 2.0
        else:
                median = combined[n//2]
        return median

        