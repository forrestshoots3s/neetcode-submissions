class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in range(strs):
            count = [0] * 26
            for c in range(s):
                count[ord(c) - ord('a')] += 1
            count = tuple(count)
            res[count].append(s)
        return list(res.values())