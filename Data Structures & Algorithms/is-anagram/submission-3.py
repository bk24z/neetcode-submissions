class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        for char in sorted(set(s)):
            s_dict[char] = s.count(char)
        for char in sorted(set(t)):
            t_dict[char] = t.count(char)
        return dict(s_dict.items()) == dict(t_dict.items())