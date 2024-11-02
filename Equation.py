class Solution:
    def __init__(self, equation: list[str]):
        self.equation = equation
        
        self.acts = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b,
            "^": lambda a, b: a ** b,
        }

    def SpaceDelete(self):
        while self.equation and self.equation[-1] == "SPACE": # while проверяет если список не пустой and проверяет если последний элемент равен "SPACE"
            self.equation.pop()


    def Act(self):
        Repeat = 0
        for FoundActs in self.equation:
            if FoundActs in self.acts.keys():
                Repeat += 1

        for _ in range(Repeat): # Повторения равно количество математических символов
            for ActIndex in range(len(self.equation)):
                if self.equation[ActIndex] in self.acts.keys():

                    # решение и вставление
                    res = self.acts[self.equation[ActIndex]](float(self.equation[ActIndex - 1]), float(self.equation[ActIndex + 1]))
                    self.equation[ActIndex] = res # заменять математический символ на ответ уравнений

                    # Чистка
                    self.equation.pop(ActIndex + 1) # удаляет число после МС
                    self.equation.append("SPACE") # кастил для избавления от "IndexError: list index out of range"

                    self.equation.pop(ActIndex - 1) # удаляет число перед МС
                    self.equation.append("SPACE") # кастил для избавления от "IndexError: list index out of range"

        self.SpaceDelete()

        

if __name__ == "__main__":
    S = Solution(["5", "/", "3"])
    S.Act()
    print(S.equation)