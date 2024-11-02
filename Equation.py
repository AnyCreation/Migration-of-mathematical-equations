class Solution:
    def __init__(self, equation: list[str]):
        self.__equation = equation
        
        self.__acts = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b,
            "^": lambda a, b: a ** b,
        }

    def SpaceDelete(self): # удаляет костыли
        while self.__equation and self.__equation[-1] == "SPACE": # while проверяет если список не пустой and проверяет если последний элемент равен "SPACE"
            self.__equation.pop()


    def Act(self):
        Repeat = 0
        for FoundActs in self.__equation:
            if FoundActs in self.__acts.keys():
                Repeat += 1

        for _ in range(Repeat): # Повторения равно количество математических символов
            for ActIndex in range(len(self.__equation)):
                if self.__equation[ActIndex] in self.__acts.keys():

                    # решение и вставление
                    res = self.__acts[self.__equation[ActIndex]](float(self.__equation[ActIndex - 1]), float(self.__equation[ActIndex + 1]))
                    self.__equation[ActIndex] = res # заменять математический символ на ответ уравнений

                    # Чистка
                    self.__equation.pop(ActIndex + 1) # удаляет число после МС
                    self.__equation.append("SPACE") # кастил для избавления от "IndexError: list index out of range"

                    self.__equation.pop(ActIndex - 1) # удаляет число перед МС
                    self.__equation.append("SPACE") # кастил для избавления от "IndexError: list index out of range"

        self.SpaceDelete()


    # возвращает результат подсчёта
    def solution(self):
        self.Act() 
        return self.__equation

        

if __name__ == "__main__":
    S = Solution(["5", "/", "3"])
    print(S.solution())