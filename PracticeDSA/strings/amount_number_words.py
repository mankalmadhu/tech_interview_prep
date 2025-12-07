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

        if n == 0:
            return "zero"
        ncrore = (n // 10000000)
        nlakh = (n // 100000) % 100
        nthousand = (n // 1000) % 100
        nten = (n // 100) % 10
        nunit = (n % 100)

        print(
            f'ncrore:{ncrore},nlakh:{nlakh},nthousand:{nthousand},nten:{nten},nunit:{nunit}'
        )

        out = ""
        out += self.numToWords(ncrore, "crore-")
        out += self.numToWords(nlakh, "lakh-")
        out += self.numToWords(nthousand, "thousand-")
        out += self.numToWords(nten, "hundred-")
        if (n > 100 and n % 100):
            out += "and-"
        out += self.numToWords(nunit, "")
        out = out[:-1]
        return out


if __name__ == "__main__":
    inputs = [12345678, 1234567, 123456, 12345, 1234, 123, 12, 1, 0]
    expected = [
        'one-crore-twenty-three-lakh-forty-five-thousand-six-hundred-and-seventy-eight',
        'twelve-lakh-thirty-four-thousand-five-hundred-and-sixty-seven',
        'one-lakh-twenty-three-thousand-four-hundred-and-fifty-six',
        'twelve-thousand-three-hundred-and-forty-five',
        'one-thousand-two-hundred-and-thirty-four',
        'one-hundred-and-twenty-three', 'twelve', 'one', 'zero'
    ]
    sol = Solution()
    for i in range(len(inputs)):
        result = sol.convertToWords(inputs[i])
        print(f'result:{result},expected:{expected[i]}')
        assert result == expected[i]
