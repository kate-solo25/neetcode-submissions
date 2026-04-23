class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} #key is the diff, value is the index
        answer = []
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen: #have we seen this key before?
                index1 = seen.get(diff)
                index2 = i
                return[index1, index2]
            seen[num] = i #searching by value and returning an index

        return []


        
