#-- INTERFAZ (LOGIN) --#
import tkinter as tk
import tkinter as ttk
from tkinter import messagebox


def iniciar(user, password):
 if user == 'PGX' and password == 'Killah2024xyz$$':
  tk.messagebox.showinfo("Exito", "Logeado exitosamente")
 else:
  tk.messagebox.showerror("Error", "Usuario o clave invalida...")

interfaz = tk.Tk()
interfaz.title("Iniciar Sesion")
interfaz.geometry("500x300")
interfaz.configure(bg="black")
interfaz.resizable(False, False)

user = tk.Label(text="Nombre de Usuario", bg="black", fg="white")
user.grid(row=0, column=0)

user_button = tk.Entry(width=20)
user_button.grid(row=0, column=1)

password = tk.Label(text="Contraseña", bg="black", fg="white")
password.grid(row=1, column=0)

password_button = tk.Entry(show="*", width=20)
password_button.grid(row=1, column=1)
px = tk.Label(text="", bg="black", fg="white")
px.grid(row=2, column=0)
btn1 = tk.Button(text="Login", command=lambda:iniciar(user_button.get(), password_button.get()), width=20)
btn1.grid(row=3, column=1)


interfaz.mainloop()
