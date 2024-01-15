class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        container = set()
        for number in nums:
            if number in container:
                return True
            container.add(number)
        return False
        