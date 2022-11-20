from tkinter import * 
from tkinter import messagebox
import tkinter as tk
from connect import Connection

class MasterPanel:

    def __init__(self):
        self.root = Tk()
        self.root.title("prueba")
        self.root.geometry("900x500")
        self.root.resizable(False, False)


        self.root.mainloop()

if __name__ == '__main__':
    MasterPanel()