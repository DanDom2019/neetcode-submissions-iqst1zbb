class Solution:
    def sort_string_alphabetically(self,s):
        return ''.join(sorted(s))

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alpha_map= {}
        i=0
        for astr in strs:
            order= self.sort_string_alphabetically(astr)
            if order not in alpha_map:
                alpha_map[order] = []
            
            alpha_map[order].append(astr)   # group words under their sorted key
        return list(alpha_map.values())     # each value is already a group
        


