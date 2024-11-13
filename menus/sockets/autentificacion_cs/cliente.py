import socket
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Función para enviar usuario y contraseña al servidor
def authenticate():
    username = entry_username.get()  # Obtener el usuario del campo de entrada
    password = entry_password.get()  # Obtener la contraseña del campo de entrada

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('localhost', 12345))  # Conectar al servidor

        # Enviar los datos del usuario y contraseña al servidor
        client_socket.send(f"{username},{password}".encode())

        # Recibir la respuesta del servidor
        response = client_socket.recv(1024).decode()

        # Mostrar un mensaje con el resultado
        messagebox.showinfo("Resultado", response)

        # Cerrar la conexión
        client_socket.close()

    except Exception as e:
        messagebox.showerror("Error", f"No se pudo conectar al servidor: {e}")

# Configuración de la interfaz gráfica (GUI)
app = tk.Tk()
app.title("Cliente de Autenticación")

# Ajustar tamaño de la ventana
app.geometry("400x300")

# Cargar la imagen de fondo (solo formatos .png o .gif)
image_path = "fari.png"  # Ruta de la imagen que quieres usar de fondo
bg_photo = tk.PhotoImage(file=image_path)

# Crear un label para la imagen de fondo
bg_label = tk.Label(app, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)  # Colocar el label que contendrá la imagen

# Etiqueta y campo de entrada para el nombre de usuario
label_username = tk.Label(app, text="Usuario:", bg='white')
label_username.pack(pady=10)
entry_username = ttk.Entry(app)
entry_username.pack()
 
# Etiqueta y campo de entrada para la contraseña
label_password = tk.Label(app, text="Contraseña:", bg='white')
label_password.pack(pady=10)
entry_password = ttk.Entry(app, show="*")
entry_password.pack()

# Botón para iniciar la autenticación
button_login = ttk.Button(app, text="Iniciar Sesión", command=authenticate)
button_login.pack(pady=20)

# Asegurarse de que los widgets estén encima de la imagen de fondo
bg_label.lower()  # Mover el fondo hacia atrás

# Iniciar el loop de la aplicación Tkinter
app.mainloop()