class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        c=1
        for num in nums:
            if num in freq:
                freq[num] +=1
            else:
                freq[num] = 1 
        frqnt = []
        for i in range(k):
            max_key = None
            max_value = 0
            for key in freq:
                if freq[key] > max_value:
                    max_value = freq[key]
                    max_key = key
            frqnt.append(max_key)
            del freq[max_key]
        return frqnt