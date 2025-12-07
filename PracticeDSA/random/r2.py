class Solution:
    one = [
        "", "one-", "two-", "three-", "four-", "five-", "six-", "seven-",
        "eight-", "nine-", "ten-", "eleven-", "twelve-", "thirteen-",
        "fourteen-", "fifteen-", "sixteen-", "seventeen-", "eighteen-",
        "nineteen-"
    ]

    # strings at index 0 and 1 are not used to make array indexing simple
    ten = [
        "", "", "twenty-", "thirty-", "forty-", "fifty-", "sixty-", "seventy-",
        "eighty-", "ninety-"
    ]

    def solve(self, A, B):
        n = (int)(A)
        y = self.convertToWords(n)

        if (y == B):
            return 1

        return 0

    # n is 1- or 2-digit number
    def numToWords(self, n, s):
        res = ""
        if (n > 19):
            res = res + self.ten[n // 10] + self.one[n % 10]
        else:
            res = res + self.one[n]

        if n:
            res = res + s

        return res

    def convertToWords(self, n):
        ncrore = (n // 10000000)
        nlakh = (n // 100000) % 100
        nthousand = (n // 1000) % 100
        nten = (n // 100) % 10
        nunit = (n % 100)

        print(ncrore)
        print(nlakh)
        print(nthousand)
        print(nten)
        print(nunit)

        out = ""
        out += self.numToWords(ncrore, "crore-")
        out += self.numToWords(nlakh, "lakh-")
        out += self.numToWords(nthousand, "thousand-")
        out += self.numToWords(nten, "hundred-")
        if (n > 100 and n % 100):
            out += "and-"
        out += self.numToWords(nunit, "")
        out = out[:-1]
        print(out)


if __name__ == "__main__":
    n = 1234
    sol = Solution()
    sol.convertToWords(n)
