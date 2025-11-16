import threading
import time

# Función que simula una tarea que toma tiempo
def process_request(request_id):
    print(f"Processing request {request_id}...")
    time.sleep(2)  # Simula una tarea que toma 2 segundos
    print(f"Request {request_id} processed.")

# Crear múltiples hilos para manejar solicitudes concurrentes
threads = []
for i in range(5):
    thread = threading.Thread(target=process_request, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All requests have been processed.")