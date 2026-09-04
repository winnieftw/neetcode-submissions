class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        history = set()
        output = {}

        for word in strs:
            sorted_chars = sorted(word)
            sorted_word = "".join(sorted_chars)
            if sorted_word not in history:
                output[sorted_word] = [word]
                history.add(sorted_word)
            else:
                output[sorted_word].append(word)
        
        return list(output.values())

