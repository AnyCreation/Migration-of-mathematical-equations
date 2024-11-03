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

    def AreaDeletion(self, OE: dict, Inse: list, HERE: list[str]):
        for Che in OE.values():
            HERE[Che[0]] ==  2
            print(Che[0])
        print(HERE)

    def SpaceCreate(self, Index, HERE: list[str]):
        HERE.pop(Index + 1) # удаляет число после МС
        HERE.append("SPACE") # кастил для избавления от "IndexError: list index out of range"

        HERE.pop(Index - 1) # удаляет число перед МС
        HERE.append("SPACE") # кастил для избавления от "IndexError: list index out of range"
        
    def SpaceDelete(self, HERE: list[str]): # удаляет костыли
        while HERE and HERE[-1] == "SPACE": # while проверяет если список не пустой and проверяет если последний элемент равен "SPACE"
            HERE.pop()

    
    def brackets(self, HERE: list[str]) -> dict: # находит позиция скобок
        OE = []
        value = {} # сохранение позиции скобак
        for Zone in range(len(HERE)):
            if HERE[Zone] == "(": # позиция открытой скобки
                OE.append(Zone)
            elif HERE[Zone] == ")": # позиция закрытой скобки
                OE.append(Zone)
        
        for V in range(0, len(OE), 2):
            value[f"O{OE[V]}E{OE[V] + 1}"]  = (OE[V], OE[V + 1])

        return value
    
    def SolutionBrackets(self, HERE: list[str]):
        Position = self.brackets(HERE)
        Equations = {}

        values = Position.values()
        for Found in range( len( Position.values() )):
            Eq = HERE[list(values)[Found][0] + 1:list(values)[Found][1]]
            Equations[f"ZONE{Found}"] = self.Act(Eq)
        print(HERE)

        return Equations
    
    def InsertionInBrackets(self, HERE: list[str]):
        Position = self.brackets(HERE)
        Insertion = self.SolutionBrackets(HERE)

        HERE = self.AreaDeletion(Position, Insertion, HERE)

        return HERE
        
        

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
    S = Solution(["58"])
    print(S.brackets(["(", "3", "^", "4", ")", "*", "(", "3", "-", "1", ")"]))
    print(S.SolutionBrackets(["(", "3", "^", "4", ")", "*", "(", "3", "-", "1", ")"]))
    print(S.InsertionInBrackets(["(", "3", "^", "4", ")", "*", "(", "3", "-", "1", ")"]))
    print(S.solution())