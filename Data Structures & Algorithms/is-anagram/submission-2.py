class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        for char in set(s):
            s_dict[char] = s.count(char)
        for char in set(t):
            t_dict[char] = t.count(char)
        return dict(sorted(s_dict.items())) == dict(sorted(t_dict.items()))