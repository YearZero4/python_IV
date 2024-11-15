import tkinter as tk


def send():
 name= input_name.get()
 lastname= input_lastname.get()
 email = input_email.get()
 year = input_year.get()
 if name != "" and name != lastname != "" and email != "" and year != "":
  print(f"Nombre : {name}\nApellido : {lastname}\nEmail: {email}\nEdad : {year}\n")

ventana = tk.Tk()
ventana.title("INTERFAZ DE USUARIO")
ventana.geometry("500x600")
ventana.config(bg="black")


name = tk.Label(ventana, text="Nombre Completo", bg="black", fg="white")
name.grid(row=0, column=0)
input_name = tk.Entry(ventana)
input_name.grid(row=0, column=1)

lastname = tk.Label(ventana, text="Apellido Completo", bg="black", fg="white")
lastname.grid(row=1, column=0)
input_lastname = tk.Entry(ventana)
input_lastname.grid(row=1, column=1)


email = tk.Label(ventana, text="Correo Electronico", bg="black", fg="white")
email.grid(row=2, column=0)
input_email = tk.Entry(ventana)
input_email.grid(row=2, column=1)


year = tk.Label(ventana, text="Edad", bg="black", fg="white")
year.grid(row=3, column=0)
input_year = tk.Entry(ventana)
input_year.grid(row=3, column=1)

close = tk.Button(ventana, text="Cerrar Interfaz", command=ventana.quit)
close.grid(row=4, column=0)

button = tk.Button(ventana, text="Enviar Datos", command=send)
button.grid(row=4, column=1)
ventana.mainloop()
