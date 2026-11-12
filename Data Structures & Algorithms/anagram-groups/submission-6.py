class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #brute force would be n^2 comparing each string
        ans = []
        hashmap = defaultdict(list)
        for word in strs:
            listWord = list(word)
            heapq.heapify(listWord)
            sortedWord = []
            while listWord:
                sortedWord.append(heapq.heappop(listWord))
            hashmap[tuple(sortedWord)].append(word) #appends the actual word, mapped to each set
        for key, value in hashmap.items():
            ans.append(value)
        return ans



        