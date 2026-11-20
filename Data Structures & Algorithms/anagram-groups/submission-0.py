class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # strs: array of strings
        # group anagrams together into sublists

        strs2 = ["".join(sorted(s)) for s in strs]
        mapping = {x: [] for x in strs2}
        
        for s in range(len(strs)):
            mapping["".join(sorted(strs[s]))].append(strs[s])
        
        return [mapping[x] for x in mapping]