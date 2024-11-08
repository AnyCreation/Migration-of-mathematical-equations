import dearpygui.dearpygui as dpg
import Equation

dpg.create_context()
W, H = 600, 800

def Solution():
    Sol = Equation.Solution(dpg.get_value("User")).solution()
    dpg.set_value("Solu", f"Solution of equation is {Sol}")

with dpg.window(label="Calculator", tag="Win"): # Window
    dpg.add_input_text(label=":Your Equation", tag="User")
    dpg.add_button(label="Solution", callback=Solution)
    dpg.add_text("Solution of equation is...", tag="Solu")


dpg.create_viewport(title='Calculator', width=W, height=H)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Win", True)
dpg.start_dearpygui()
dpg.destroy_context()