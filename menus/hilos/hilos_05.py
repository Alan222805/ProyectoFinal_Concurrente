import threading, random
from time import sleep

def ejecutar():
    print(f'Comienza {threading.current_thread().name}')
    sleep(random.random())
    print(f'Termina {threading.current_thread().name}')

hilo1 = threading.Thread(target=ejecutar, name='Hilo 1')
hilo2 = threading.Thread(target=ejecutar, name='Hilo 2')

hilo1.start()
hilo2.start()

#El hilo principal si espera por el resto de hilos
hilo1.join()
hilo2.join()

print('El hilo principal si espera por el resto de hilos')