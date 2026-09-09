class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #return in asc order
        #cant use duplicted index
        store=defaultdict(list)
        n=len(numbers)
        for i in range(n):
            require=target-numbers[i]
            if require in store:
                return [store[require][0],i+1]
            store[numbers[i]].append(i+1)
        
