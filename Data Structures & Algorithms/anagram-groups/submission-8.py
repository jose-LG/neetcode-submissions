class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        count = [0] * 26
        for word in strs:
            for char in word:
                count[ord(char) - ord("a")] += 1 #adding one to correspponding letter
            hashmap[tuple(count)].append(word)
            count = [0] * 26
        ans = []
        for values in hashmap.values():
            ans.append(values)
        return ans

        