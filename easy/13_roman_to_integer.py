class Solution:
    base = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    def romanToInt(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            if i < len(s) - 1 and self.base[s[i]] < self.base[s[i + 1]]:
                res -= self.base[s[i]]
            else:
                res += self.base[s[i]]

        return res


class Solution2:
    def romanToInt(self, s: str) -> int:
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        res = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for x in s:
            res += translations[x]
        return res


if __name__ == "__main__":
    print(Solution2().romanToInt('XXXIX'))
