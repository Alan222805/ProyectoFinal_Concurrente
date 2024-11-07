import tkinter as tk
from tkinter import Menu

# Lista de apartados principales del menú
apartados = ["Hilos", "Sockets", "Semaforos", "Patrones", "Documentacion", "Ayuda", "Salir"]

# Crear la ventana principal
root = tk.Tk()
root.title("Interfaz con Menú")  # Título de la ventana
root.geometry("1920x1080")  # Tamaño de la ventana

# Agregar un título en la ventana
label_title = tk.Label(root, text="Bienvenido a la Interfaz", font=("Arial", 40))
label_title.pack(pady=10)

# Crear el menú principal
menu_bar = Menu(root)

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
        "Autentificación C -> S"
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

# Crear los apartados en el menú
for apartado in apartados:
    menu = Menu(menu_bar, tearoff=0)
    
    # Añadir subapartados si existen para el apartado actual
    if apartado in subapartados:
        for subapartado in subapartados[apartado]:
            menu.add_command(label=subapartado)
        menu.add_separator()  # Separador entre el último subapartado y el final del menú
    
    # Añadir opción de Salir si el apartado es "Salir"
    if apartado == "Salir":
        menu.add_command(label="Salir", command=root.quit)

    # Añadir el menú al menú principal
    menu_bar.add_cascade(label=apartado, menu=menu)

# Configurar la barra de menú en la ventana
root.config(menu=menu_bar)

# Iniciar el bucle principal de la aplicación
root.mainloop()
