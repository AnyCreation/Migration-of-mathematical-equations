class Solution:
    def __init__(self, equation: list[str] | str):
        if isinstance(equation, str):
            self.__equation = equation.split(" ")
        else:
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



    # (!--костил--!)
    def SpaceCreate(self, Index, HERE: list[str]):

        """
        - присоединение двух чисел происходит изменение количества элементов что иногда приводит к IndexError

        ↓

        - добавляя "запасной" элемент в конец списка ошибка избегается
        """

        HERE.pop(Index + 1) # удаляет число после МС
        HERE.append("SPACE") # кастил для избавления от "IndexError: list index out of range"

        HERE.pop(Index - 1) # удаляет число перед МС
        HERE.append("SPACE") # кастил для избавления от "IndexError: list index out of range"
        
    def SpaceDelete(self, HERE: list[str]): # удаляет костыли
        """
        - зная точно что запасной элемент будет в конце списка 
        - я могу его удалить без боязни что удалиться какой-то важный элемент
        """

        while HERE and HERE[-1] == "SPACE": # while проверяет если список не пустой and проверяет если последний элемент равен "SPACE"
            HERE.pop()
    # (!--костил--!)


    # (!--скобки--!)
    def AreaDeletion(self, Pos: list, Inse: list, HERE: list[str]):
        """
        ***AreaDeletion***
        - Pos - позиция открытой и закрытой скобки
        - Inse - значение согласно уравнению внутри скобок
        - HERE - общее уравнение

        вставляет ответ скобок и удаляет скобки и всё что внутри них
        """

        Deletes = []

        for Area in Pos:
            HERE[Area[ 0]] = Inse[Pos.index(Area)][-1] # ставить решения скобок вместо первой скобки

            for delete in range(Area[0] + 1, Area[1] + 1): # начинает от первого элемента после открытой скобки и заканчивает на закрытую скобку
                Deletes.append(delete) # сохранять места которые должны быть удалены

        for D in Deletes[::-1]: # проходеть по местом удаления от конца до начало, для избегание IndexError: pop index out of range
            HERE.pop(D) # удаляет элемент по индексу

        return HERE

    def brackets(self, HERE: list[str]) -> dict: # находит позиция скобок
        OE = [] # сохранение индекса скобок
        value = [] # сохранение позиции скобак
        for Zone in range(len(HERE)):
            if HERE[Zone] == "(": # позиция открытой скобки
                OE.append(Zone)
            elif HERE[Zone] == ")": # позиция закрытой скобки
                OE.append(Zone)
        
        for Convert in range(0, len(OE), 2):
            # сохраняет в одном кортеже индекс открытой и индекс закрытой скобки
            value.append((OE[Convert], OE[Convert + 1])) 

        return value
    
    
    def SolutionBrackets(self, HERE: list[str]):
        Position = self.brackets(HERE) # получает индекс скобок
        Equations = [] # список для сохранения решений

        for Found in range( len( Position )):
            Eq = HERE[Position[Found][0] + 1:Position[Found][1]] # решает уравнение внутри скобок
            Equations.append(self.Act(Eq, False)) # сохраняет решение уравнения | проверка что подсчёт вне скобок (почёт в скобках Так что False)
            
        return Equations, Position
    
    def InsertionInBrackets(self, HERE: list[str]):
        Insertion, Position = self.SolutionBrackets(HERE)
        HERE = self.AreaDeletion(Position, Insertion, HERE) # вставляет ответ в общее уравнение

        return HERE
    # (!--скобки--!)
        

    def Act(self, EQUA: list[str], Out: bool):
        if Out: # проверяйте если уравнение для подсчёта вне скобок
            EQUA = self.InsertionInBrackets(EQUA)
        
        Repeat = 0
        for FoundActs in EQUA:
            if FoundActs in self.__mathSymbols:
                Repeat += 1

        lenEquation = range(len(EQUA))

        # сперва решаеть степень
        for _ in range(Repeat): # Повторения равно количество математических символов в уравнении
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
        result = self.Act(self.__equation, True) 
        return result

        

if __name__ == "__main__":
    S = Solution(["58", "*", "(", "1", "-", "1", ")", "+", "10"])
    print(S.solution())