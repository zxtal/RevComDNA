from appViews import InputComponent, OutputComponent
import tkinter as tk

def start_app():
    root = tk.Tk()
    root.title("DNA Sequence Manipulator")
    root.geometry("800x400")
    root.config(relief=tk.SUNKEN)
    InputComponent(root)
    OutputComponent(root)
    root.mainloop()

if __name__ == "__main__":
    start_app()

