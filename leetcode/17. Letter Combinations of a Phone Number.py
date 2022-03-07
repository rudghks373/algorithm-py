class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            '2' : ['a','b','c'],
            '3' : ['d','e','f'],
            '4' : ['g','h','i'],
            '5' : ['j','k','l'],
            '6' : ['m','n','o'],
            '7' : ['p','q','r','s'],
            '8' : ['t','u','v'],
            '9' : ['w','x','y','z']
        }
        if digits == "": return []
        solution = ['']
        for digit in digits:
            solution = [prev + char for prev in solution for char in mapping[digit]]
        return solution
