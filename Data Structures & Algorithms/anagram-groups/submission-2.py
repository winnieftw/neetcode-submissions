class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
            words: {
                "aht": ["aht"],
                "act": ["act", "cat"].
                "opst": ["stop", "pots", "tops"]
            }
        '''

        if len(strs) == 0:
            return [[""]]
        elif len(strs) == 1:
            return [strs]
        else:
            words = {}

            for word in strs:
                s_word = ''.join(sorted(word))
                if s_word not in words:
                    words[s_word] = [word]
                else:
                    words[s_word].append(word)
            return list(words.values())

        return []
        