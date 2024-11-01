class Solution:
    def __init__(self, equation: list[str]):
        self.equation = equation
        self.sym = {}
        self.Found()

    def Found(self):
        self.sym.clear()
        S = ["+", "-", "*", "/", "^"]
        for C in range(len(self.equation)):
            if self.equation[C] in S:
                self.sym[C] = self.equation[C]

    def Act(self):
        act = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b,
            "^": lambda a, b: a ** b,
        }
        
        self.Found()
        for i in self.sym.keys():
            print(self.equation[i])
            Result = act[self.equation[i]](float(self.equation[i - 1]), float(self.equation[i + 1]))
            self.equation[i] = Result
            self.equation.pop(i + 1)
            self.equation.pop(i - 1)
        return self.equation

if __name__ == "__main__":
    S = Solution(["2", "+", "12", "-", "5"])
    print(S.Act())