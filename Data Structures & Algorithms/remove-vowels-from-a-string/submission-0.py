class Solution:
    def removeVowels(self, s: str) -> str:
        array = []
        vowels = set(['a', 'e', 'i', 'o', 'u'])

        for i, char in enumerate(s):
            if char not in vowels:
                array.append(char)
        return "".join(array)