class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # have a loop to go through both strings and store them in dictionary
        # get the values created from the dictionary to determine if there are any discrepancies

        if len(s) == len(t):
            s_dict = {}
            t_dict = {}

            for index in range(len(s)):
                s_val = s[index]
                t_val = t[index]

                if s_val in s_dict:
                    s_dict[s_val] += 1
                else:
                    s_dict[s_val] = 1
                if t_val in t_dict:
                    t_dict[t_val] += 1
                else:
                    t_dict[t_val] = 1


            return s_dict == t_dict
        return False