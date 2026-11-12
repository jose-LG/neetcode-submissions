class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #any two sorted words that equal eachother are anaggrams
        #We can sort eachw ord in the list and compare words to eachother
            #Sorting would take m * nlogn time because we have to do it m times
        
        #Can sort each word and take the alphabet count of each one

        #For example each word can have an array of 1-26 represenitng the counts of chars
        #if we have this equal the key, we can append any word to our defaultdict(list)s

        grouping = defaultdict(list)
        ans = []

        for word in strs:
            alphaCount = [0] * 26 #reset for every word, we want a unique one
            for char in word:
                matchingLetterToIndex = abs(ord('a') - ord(char)) #0-26
                alphaCount[matchingLetterToIndex] += 1
            #now we have a full map of the alphaCount for said "word"
            #Leverage our defaultDict list and simply update the count for that key
            #keep in the first for loop because we want every word to be appended
            grouping[tuple(alphaCount)].append(word)
        
        #now we can return the lists found n grouping

        for groupList in grouping.values():
            ans.append(groupList)
        return ans
            