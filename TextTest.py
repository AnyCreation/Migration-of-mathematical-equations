import Equation

Text = input("Enter equation: ").split(" ")
E = Equation.Solution(Text)
print(E.solution())

x = lambda: 3 * 4
print(x())