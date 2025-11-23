from collections import deque

def manage_delivery_queue():
    """
    Crea una cola para gestionar entregas utilizando deque de la librería collections.

    Returns:
    list: A list.
    """
    delivery_queue = deque(["Pedido 1", "Pedido 2", "Pedido 3"])
    delivery_queue.append("Pedido 4")  # Agregar un nuevo pedido al final de la cola
    delivery_queue.appendleft("Pedido Urgente")  # Agregar un pedido urgente al inicio de la cola
    delivery_queue.pop()  # Procesar el último pedido
    delivery_queue.popleft()  # Procesar el pedido más urgente
    return delivery_queue

queue = manage_delivery_queue()
print("Cola de entregas actual:", queue)