import subprocess
import tkinter as tk
from tkinter import Menu
import os

# Lista de apartados principales del menú
apartados = ["Hilos", "Sockets", "Semaforos", "Patrones", "Documentacion", "Ayuda", "Salir"]

# Subapartados para cada apartado del menú
subapartados = {
    "Hilos": [
        "Hilos", 
        "Hilos aumentos", 
        "Hilos función tarea", 
        "Hilos sincronización", 
        "Mario Bros Roleta"
    ],
    "Sockets": [
        "Mensajes C -> S", 
        "TCP -> C -> S", 
        "UDP -> C -> S", 
        "Comunicación Directa", 
        "Comunicación Indirecta", 
        "Autentificación cs"
    ],
    "Semaforos": [
        "Sincronización Semáforos", 
        "Semáforos C -> S", 
        "Condición de Carrera", 
        "Barbero Dormilón", 
        "Barbero Dormilón C -> S", 
        "Sala de Chat"
    ],
    "Patrones": [
        "Future-Promise", 
        "Productor-Consumidor", 
        "Actor", 
        "Reactor y Proactor"
    ]
}

# Función para abrir el una ventana flotante
def abrir_ventana(archivo, carpeta=None):
    ruta = os.path.join("menus", carpeta or "", f"{archivo}.py")
    subprocess.Popen(["python", ruta])


# Función para crear un menú con subapartados
def crear_menu(apartado, root):
    menu = Menu(root, tearoff=0)

    if apartado in subapartados:
        for subapartado in subapartados[apartado]:
            menu.add_command(label=subapartado, command=lambda: abrir_ventana(subapartado.lower().replace(" ", "_"), apartado.lower())) 
        menu.add_separator()
    
    if apartado == "Salir":
        menu.add_command(label="Salir", command=root.quit)

    if apartado == "Ayuda":
        menu.add_command(label="Abrir Ayuda", command=lambda: abrir_ventana("ayuda"))
    return menu

# Función para configurar la ventana principal
def configurar_ventana(root):
    root.title("Interfaz con Menú")
    root.geometry("1920x1080")
    label_title = tk.Label(root, text="Proyecto final\nProgramacion concurrente", font=("Arial", 40))
    label_title.pack(pady=10)

# Función principal para crear la interfaz
def main():
    root = tk.Tk()
    configurar_ventana(root)
    menu_bar = Menu(root)
    for apartado in apartados:
        menu = crear_menu(apartado, root)
        menu_bar.add_cascade(label=apartado, menu=menu)
    root.config(menu=menu_bar)
    root.mainloop()

if __name__ == "__main__":
    main()
