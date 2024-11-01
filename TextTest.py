import Equation

Text = input("Enter equation: ").split(" ")
E = Equation.Solution(Text)
E.Act()
print(E.equation)