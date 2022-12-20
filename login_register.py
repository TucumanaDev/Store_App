from tkinter import * 
from tkinter import messagebox
import tkinter as tk
from connect import Connection
from user import User

class LoginPanel:

    _INSERT = "insert into users(name, lastname, ci, passwd, rol) values (%s, %s, %s, %s, %s)"

    def insertUser(self, user, lastname, ci, password, rol):
        with Connection.getConnection():
            with Connection.getCursor() as cursor:
                values = (user, lastname, ci, password, rol)
                cursor.execute(self._INSERT, values)
                register = cursor.rowcount   
        return register 

    def __init__(self):
        self.root = Tk()
        self.root.title("prueba")
        self.root.geometry("900x500")
        self.root.resizable(False, False)

        self.username = StringVar()
        self.password = StringVar()
        self.ci = StringVar()
        self.lastname = StringVar()

        label_one = Label(self.root, text="REGISTRO", font=("Helvetica", 30, 'bold'), fg="black")
        label_one.place(x=330, y=60)

        label_usr = Label(self.root, text="Nombre", font=("Helvetica", 10, 'bold'), fg="black")
        label_usr.place(x=50, y=160)

        text_field_usr = Entry(self.root, justify="center", width=21, font=("poppins", 25, "bold"), bg="#404040", border=0, fg="white", textvariable=self.username)
        text_field_usr.place(x=50, y=190)
        text_field_usr.focus() 

        label_lstnm = Label(self.root, text="Carnet de identidad", font=("Helvetica", 10, 'bold'), fg="black")
        label_lstnm.place(x=450, y=160)

        text_field_lastname= Entry(self.root, justify="center", width=21, font=("poppins", 25, "bold"), bg="#404040", border=0, fg="white", textvariable=self.lastname)
        text_field_lastname.place(x=50, y=290)
        text_field_lastname.focus()

        label_ci = Label(self.root, text="Apellido", font=("Helvetica", 10, 'bold'), fg="black")
        label_ci.place(x=50, y=260)

        text_field_ci = Entry(self.root, justify="center", width=21, font=("poppins", 25, "bold"), bg="#404040", border=0, fg="white", textvariable=self.ci)
        text_field_ci.place(x=450, y=190)
        text_field_ci.focus()

        label_psswd = Label(self.root, text="Contraseña", font=("Helvetica", 10, 'bold'), fg="black")
        label_psswd.place(x=450, y=260)


        text_field_passwd = Entry(self.root, justify="center", width=21, font=("poppins", 25, "bold"), bg="#404040", border=0, fg="white",textvariable=self.password)
        text_field_passwd.place(x=450, y=290)
        text_field_passwd.focus()       

        send_data = Button(self.root, text="Registrar", font=("poppins", 20, "bold"), bg="black", fg="grey", command = self.register_user)
        send_data.place(x=360, y=370)

        self.root.mainloop()


    def register_user(self):
        self.user = self.username.get()
        self.lstname = self.lastname.get()
        self.carnet = self.ci.get()
        self.passwd = self.password.get()

        print ("Nombre: {}\nApellido: {}\nCarnet: {}\nPassword: {}".format(self.user, self.lstname, self.carnet, self.passwd))

        usuario = User(name=self.user, lastaname=self.lstname, ci=self.carnet, password=self.passwd)
        print(usuario)

        insert_user = self.insertUser(usuario.name, usuario.lastname, usuario.ci, usuario.password, usuario.rol)
        print(  insert_user)        
if __name__ == '__main__':
    LoginPanel()
    