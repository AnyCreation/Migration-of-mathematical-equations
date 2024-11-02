class Solution:
    def __init__(self, equation: list[str]):
        self.__equation = equation

        self.__mathSymbols = ("+", "-", "*", "/", "^")
        self.__MINacts = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
        }
        self.__MIDacts = {
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b,
        }
        self.__MAXacts = {
            "^": lambda a, b: a ** b,
        }

    def SpaceCreate(self, Index):
        self.__equation.pop(Index + 1) # удаляет число после МС
        self.__equation.append("SPACE") # кастил для избавления от "IndexError: list index out of range"

        self.__equation.pop(Index - 1) # удаляет число перед МС
        self.__equation.append("SPACE") # кастил для избавления от "IndexError: list index out of range"
        
    def SpaceDelete(self): # удаляет костыли
        while self.__equation and self.__equation[-1] == "SPACE": # while проверяет если список не пустой and проверяет если последний элемент равен "SPACE"
            self.__equation.pop()


    def Act(self):
        Repeat = 0
        for FoundActs in self.__equation:
            if FoundActs in self.__mathSymbols:
                Repeat += 1

        lenEquation = range(len(self.__equation))
        # сперва решаеть степень
        for _ in range(Repeat): # Повторения равно количество математических символов
            for ActIndex in lenEquation:
                # ^
                if self.__equation[ActIndex] in self.__MAXacts.keys():
                    # решение и вставление
                    res = self.__MAXacts[self.__equation[ActIndex]](float(self.__equation[ActIndex - 1]), float(self.__equation[ActIndex + 1]))
                    self.__equation[ActIndex] = res # заменять математический символ на ответ уравнений

                    self.SpaceCreate(ActIndex)

        # потом решаеть умножения и деления
        for _ in range(Repeat): # Повторения равно количество математических символов
            for ActIndex in lenEquation:
                # *; /
                if self.__equation[ActIndex] in self.__MIDacts.keys():
                    # решение и вставление
                    res = self.__MIDacts[self.__equation[ActIndex]](float(self.__equation[ActIndex - 1]), float(self.__equation[ActIndex + 1]))
                    self.__equation[ActIndex] = res # заменять математический символ на ответ уравнений

                    self.SpaceCreate(ActIndex)

        # напоследок решает плюс и минус
        for _ in range(Repeat): # Повторения равно количество математических символов
            for ActIndex in lenEquation:
                # +; -
                if self.__equation[ActIndex] in self.__MINacts.keys():

                    # решение и вставление
                    res = self.__MINacts[self.__equation[ActIndex]](float(self.__equation[ActIndex - 1]), float(self.__equation[ActIndex + 1]))
                    self.__equation[ActIndex] = res # заменять математический символ на ответ уравнений

                    self.SpaceCreate(ActIndex)

        self.SpaceDelete()


    # возвращает результат подсчёта
    def solution(self):
        self.Act() 
        return self.__equation

        

if __name__ == "__main__":
    S = Solution(["3", "^", "4", "*", "3"])
    print(S.solution())