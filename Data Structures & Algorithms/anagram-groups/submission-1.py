class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # strs: array of strings
        # group anagrams together into sublists
        
        # Mapping character count to list of Anagrams
        result = defaultdict(list) # the default value is a list

        for s in strs: 
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1
            
            result[tuple(count)].append(s) # Lists cannot be keys
            
        return [x for x in result.values()]

    '''
        strs2 = ["".join(sorted(s)) for s in strs]
        mapping = {x: [] for x in strs2}
        
        for s in range(len(strs)):
            mapping["".join(sorted(strs[s]))].append(strs[s])
        
        return [mapping[x] for x in mapping]
        '''