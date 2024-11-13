import socket

# Almacenar usuarios y contraseñas en un diccionario
users = {
    "usuario1": "password1",
    "usuario2": "password2",
    "usuario3": "password3",
    "usuario4": "password4",
    "usserslalo": "Userslalo#467"
}

# Configuración del servidor
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))  # Dirección y puerto del servidor
    server_socket.listen(5)  # Escuchar un máximo de 5 conexiones entrantes

    print("Servidor iniciado. Esperando conexiones...")

    while True:
        # Esperar a que un cliente se conecte
        client_socket, address = server_socket.accept()
        print(f"Conexión aceptada de {address}")

        # Recibir usuario y contraseña del cliente
        data = client_socket.recv(1024).decode()  # Recibir datos del cliente
        username, password = data.split(',')  # Dividir los datos recibidos

        # Autenticar usuario
        if username in users and users[username] == password:
            response = "Autenticación exitosa"
        else:
            response = "Autenticación fallida"

        # Enviar respuesta al cliente
        client_socket.send(response.encode())
        client_socket.close()

if __name__ == "__main__":
    start_server()
