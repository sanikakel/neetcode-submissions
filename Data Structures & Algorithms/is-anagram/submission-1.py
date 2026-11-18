class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # anagrams: 2 strings have the same characters with each char appearing the same amount of times

        map = {}

        for x in s:
            if x in map:
                map[x] += 1
            else:
                map[x] = 1
        
        for y in t:
            if y in map:
                map[y] -= 1
            else:
                return False
        
        return all([map[i] == 0 for i in map])
