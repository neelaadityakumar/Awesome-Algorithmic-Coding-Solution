from sortedcontainers import SortedList


class Solution:
    def maxSlidingWindow(self, nums, k):
        s = SortedList(nums[:k])
        ret = []

        for i in range(k, len(nums)):
            ret.append(s[-1])
            s.remove(nums[i - k])
            s.add(nums[i])

        ret.append(s[-1])
        return ret
