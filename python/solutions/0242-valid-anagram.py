class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_hash = {}
        t_hash = {}

        i = 0
        while i < len(s):
            s_letter = s[i]
            t_letter = t[i]

            if not s_hash.get(s_letter):
                s_hash[s_letter] = 0
            s_hash[s_letter] += 1

            if not t_hash.get(t_letter):
                t_hash[t_letter] = 0
            t_hash[t_letter] += 1

            i += 1
        return s_hash == t_hash


if __name__ == "__main__":
    sol = Solution()

    testcases = [
        ("anagram", "nagaram", True),
        ("cat", "rat", False),
        ("alpha", "alph", False),
    ]

    for test in testcases:
        s, t = test[0], test[1]
        expected = test[2]
        result = sol.isAnagram(s, t)
        print(f"Result: {result}, Expected: {expected}")
