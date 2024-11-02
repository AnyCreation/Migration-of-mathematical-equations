import Equation

Text = input("Enter equation: ").split(" ")
E = Equation.Solution(Text)
print(E.solution())