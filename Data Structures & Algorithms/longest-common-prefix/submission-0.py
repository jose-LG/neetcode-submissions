class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #We can store in a hashmap every type of ocruance for the first word
        #Intuition: if its the longest common, it must also exist in the first string

        prefixes = {}
        runningString = ""
        for char in strs[0]:
            runningString = runningString + char
            prefixes[runningString] = 1 
        
        #{"d": 1, "da": 2}
        #we want to return "da"
        longestPrefix = ""
        for i in range(1, len(strs)):
            word = strs[i]
            compString = ""
            for char in word:
                compString = compString + char
                if compString in prefixes:
                    prefixes[compString] = prefixes.get(compString) + 1

        for key, value in prefixes.items():
            if value == len(strs):
                longestPrefix = key
        

        return longestPrefix