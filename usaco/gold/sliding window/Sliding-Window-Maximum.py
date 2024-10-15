from typing import List
from sortedcontainers import SortedList
import collections
# with sorted list


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

# with deque
# montonic decreasing queue
    def maxSlidingWindow(self, nums: List[int], k: int) -> list[int]:
        d = collections.deque()

        def enqueue(i: int) -> None:
            while d and nums[d[-1]] <= nums[i]:
                d.pop()
            d.append(i)
            while d and (i - d[0]) >= k:
                d.popleft()

        ret = []
        for i in range(len(nums)):
            enqueue(i)
            if i + 1 >= k:
                ret.append(nums[d[0]])
        return ret


# with max queue , two stacks

class MaxQueue:
    def __init__(self):
        """
        For each pair (val, max_val) in the stacks:
        - val: The value of the element.
        - max_val: The maximum among all elements in that stack under element val.
        """
        self.s1 = []
        self.s2 = []

    def query(self) -> int:
        """
        Get the maximum element in the MaxQueue.
        It is the maximum of both stacks, stored in the second value of the top of the stack.
        """
        if not self.s1 and not self.s2:
            return float("-inf")
        if not self.s1 or not self.s2:
            return self.s2[-1][1] if not self.s1 else self.s1[-1][1]
        return max(self.s1[-1][1], self.s2[-1][1])

    """
    	Add a new element into the MaxQueue. We add the value of this
    	element and the maximum element in stack s1 after adding.
    	"""

    def enqueue(self, val: int):
        max_val = max(val, self.s1[-1][1]) if self.s1 else val
        self.s1.append((val, max_val))

    """
    	Remove the first element from our MaxQueue by poping the top
    	element from s2.
    	"""

    def dequeue(self):
        # Move all elements from s1 to s2 when s2 is empty
        if not self.s2:
            while self.s1:
                val = self.s1.pop()[0]
                max_val = max(val, self.s2[-1][1]) if self.s2 else val
                self.s2.append((val, max_val))
        self.s2.pop()


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        q = MaxQueue()
        max_vals = []

        # Fill the queue with elements from the first window
        for i in range(k):
            q.enqueue(nums[i])
        max_vals.append(q.query())

        """
		We slide the window to the right by removing the first element
		from the queue and adding the new element at the end of the queue.
		For each window, we add the maximum to our result array max_vals.
		"""
        for i in range(k, len(nums)):
            q.dequeue()
            q.enqueue(nums[i])
            max_vals.append(q.query())

        return max_vals
