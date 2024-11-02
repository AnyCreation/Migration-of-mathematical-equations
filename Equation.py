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


    def SpaceCreate(self, Index, HERE: list[str]):
        HERE.pop(Index + 1) # удаляет число после МС
        HERE.append("SPACE") # кастил для избавления от "IndexError: list index out of range"

        HERE.pop(Index - 1) # удаляет число перед МС
        HERE.append("SPACE") # кастил для избавления от "IndexError: list index out of range"
        
    def SpaceDelete(self, HERE: list[str]): # удаляет костыли
        while HERE and HERE[-1] == "SPACE": # while проверяет если список не пустой and проверяет если последний элемент равен "SPACE"
            HERE.pop()


    def Act(self, EQUA: list[str]):
        Repeat = 0
        for FoundActs in EQUA:
            if FoundActs in self.__mathSymbols:
                Repeat += 1

        lenEquation = range(len(EQUA))

        # сперва решаеть степень
        for _ in range(Repeat): # Повторения равно количество математических символов
            for ActIndex in lenEquation:
                # ^
                if EQUA[ActIndex] in self.__MAXacts.keys():
                    # решение и вставление
                    res = self.__MAXacts[EQUA[ActIndex]](float(EQUA[ActIndex - 1]), float(EQUA[ActIndex + 1]))
                    EQUA[ActIndex] = res # заменять математический символ на ответ уравнений

                    self.SpaceCreate(ActIndex, EQUA)

        # потом решаеть умножения и деления
        for _ in range(Repeat): # Повторения равно количество математических символов
            for ActIndex in lenEquation:
                # *; /
                if EQUA[ActIndex] in self.__MIDacts.keys():
                    # решение и вставление
                    res = self.__MIDacts[EQUA[ActIndex]](float(EQUA[ActIndex - 1]), float(EQUA[ActIndex + 1]))
                    EQUA[ActIndex] = res # заменять математический символ на ответ уравнений

                    self.SpaceCreate(ActIndex, EQUA)

        # напоследок решает плюс и минус
        for _ in range(Repeat): # Повторения равно количество математических символов
            for ActIndex in lenEquation:
                # +; -
                if EQUA[ActIndex] in self.__MINacts.keys():

                    # решение и вставление
                    res = self.__MINacts[EQUA[ActIndex]](float(EQUA[ActIndex - 1]), float(EQUA[ActIndex + 1]))
                    EQUA[ActIndex] = res # заменять математический символ на ответ уравнений

                    self.SpaceCreate(ActIndex, EQUA)
        self.SpaceDelete(EQUA)

        return EQUA


    # возвращает результат подсчёта
    def solution(self):
        result = self.Act(self.__equation) 
        return result

        

if __name__ == "__main__":
    S = Solution(["3", "^", "4", "*", "3"])
    print(S.solution())