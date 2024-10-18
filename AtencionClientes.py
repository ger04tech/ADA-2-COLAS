from collections import deque


colas = {
    1: deque(),
    2: deque(),
    3: deque()
}


def encolar_cliente(servicio):
    if servicio in colas:
        numero_cliente = len(colas[servicio]) + 1
        colas[servicio].append(numero_cliente)
        print(f"Cliente {numero_cliente} agregado a la cola del servicio {servicio}.")
    else:
        print(f"El servicio {servicio} no existe.")


def atender_cliente(servicio):
    if servicio in colas and colas[servicio]:
        numero_atendido = colas[servicio].popleft()
        print(f"Atendiendo al cliente {numero_atendido} del servicio {servicio}.")
    else:
        print(f"No hay clientes en la cola del servicio {servicio}.")


while True:
    accion = input("Escribe 'c' para encolar un cliente o 'a' para atender un cliente (o 'q' para salir): ").lower()

    if accion == 'q':
        print("Saliendo del sistema.")
        break

    if accion in ['c', 'a']:
        try:
            servicio = int(input("Escribe el número del servicio (1, 2 o 3): "))
        except ValueError:
            print("Número de servicio inválido. Debe ser 1, 2 o 3.")
            continue

        if accion == 'c':
            encolar_cliente(servicio)
        elif accion == 'a':
            atender_cliente(servicio)
    else:
        print("Opción no reconocida, intenta de nuevo.")
