class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for word in strings:
            currTuple = []
            for i in range(1, len(word)):
                diff = (ord(word[i]) - ord(word[i - 1])) % 26
                currTuple.append(diff)
            #add current word into the bucket it needs to go into
            hashmap[tuple(currTuple)].append(word)
        #now that we have all of the tuples in order, we can simply append all lists/values in hashmap into one large list
        ans = []
        for wordList in hashmap.values():
            ans.append(wordList)
        return ans