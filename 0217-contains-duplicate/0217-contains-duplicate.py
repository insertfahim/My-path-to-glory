class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        my_set = set()
        for number in nums:
            if number in my_set:
                return True
            else:
                my_set.add(number)
        return False