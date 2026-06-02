class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        d = {'2' : set('abc'),
             '3' : set('def'),
             '4' : set('ghi'),
             '5' : set('jkl'),
             '6' : set('mno'),
             '7' : set('pqrs'),
             '8' : set('tuv'),
             '9' : set('wxyz')}
        op = [""]
        for i in digits:
            L = []
            for j in op:
                for k in d[i]:
                    L.append(j + k)
            op = L[:]
        return op