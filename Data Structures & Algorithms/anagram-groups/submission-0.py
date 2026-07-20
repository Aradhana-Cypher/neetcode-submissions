class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}
        for wrd in strs:
            key = "".join(sorted(wrd))
            if key not in freq:
              freq[key] = []
            freq[key].append(wrd)
        return list(freq.values())


        