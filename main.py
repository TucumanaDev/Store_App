from tkinter import * 
from tkinter import messagebox
import tkinter as tk
from connect import Connection
from masterpanel import MasterPanel
from login_register import LoginPanel

class LoginUser():
    # Cambiar la consulta 
    _SELECT = "select * from users where name=%s and password=%s"
    _validation = False
    
    def selectUser(self, username_data, password_data):
        cursor = Connection.getCursor()
        values = (username_data, password_data)
        cursor.execute(self._SELECT, values)
        register = cursor.fetchone()
        if register is None:
            messagebox.showerror(message="Usuario o Contraseña incorrectos", title="Error")
        
        else:
            self.root.destroy()
            MasterPanel()
            return register

    def register_user(self):
        LoginPanel()



    def __init__(self):
        self.root = Tk()
        self.root.title("prueba")
        self.root.geometry("900x500")
        self.root.resizable(False, False)

        if LoginUser._validation == True:
            self.root.destroy()
            MasterPanel()
        
        self.username = StringVar()
        self.password = StringVar()

        label_one = Label(self.root, text="LOGIN", font=("Helvetica", 45, 'bold'), fg="black")
        label_one.place(x=340, y=100)

        user_image = PhotoImage(file="images/search.png")
        user_label = Label(image=user_image)
        user_label.place(x=200, y=170)

        passwd_image = PhotoImage(file="images/search.png")
        passwd_label = Label(image=passwd_image)
        passwd_label.place(x=200, y=270)

        text_field_usr = Entry(self.root, justify="center", width=21, font=("poppins", 25, "bold"), bg="#404040", border=0, fg="white", textvariable=self.username)
        text_field_usr.place(x=250, y=190)
        text_field_usr.focus()

        text_field_passwd = Entry(self.root, justify="center", width=21, font=("poppins", 25, "bold"), bg="#404040", border=0, fg="white", show="*", textvariable=self.password)
        text_field_passwd.place(x=250, y=290)
        text_field_passwd.focus()

        send_data = Button(self.root, text="enviar", font=("poppins", 25, "bold"), bg="black", fg="grey", command=self.login_user)
        send_data.place(x=530, y=370)

        send_data = Button(self.root, text="Registrar", font=("poppins", 25, "bold"), bg="black", fg="grey", command=self.register_user)
        send_data.place(x=230, y=370)

        self.root.mainloop()

    def login_user(self):
        self.username_data = self.username.get()
        self.password_data = str(self.password.get())
        print("Usuario: {}\n" 
            "Contraseña: {}".format(self.username_data, self.password_data))
        reg =self.selectUser(self.username_data, self.password_data)
        print(reg)


if __name__ == "__main__":
    LoginUser()
    
# Algunas variables no era reconocidas correctamente por la ausencia de "self"
#añadiendo un comentario de prueba para comprobar funcionamiento de github. 