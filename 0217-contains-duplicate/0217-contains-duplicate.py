class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        container = set()
        for item in nums:
            if item not in container:
                container.add(item)
            else:
                return True
        return False