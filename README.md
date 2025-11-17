# platzi_python_0010_curso
platzi_python_0010_curso

# Entorno virtual con uv
## Crear entorno virtual
```:bash
uv --version
```
```:bash
uv init
```
```:bash
uv venv
```


# Curso 0010
- [Estructuras de Datos Avanzadas en Python: Collection y Enumeraciones](https://platzi.com/cursos/python/libreria-collections-y-enumeraciones/)
    - Collections : deque (Uso de colas)
    [manage_delivery_queue.py](manage_delivery_queue.py)
    - Collections : enumerate (Uso de enumeraciones)
    [order_status.py](order_status.py)
    - Collections : defaultdict (Uso de diccionarios con valores por defecto)
    [count_products.py](count_products.py)
    - Collections : counter (Conteo de elementos)
    [most_common_products.py](most_common_products.py)
    [counter_string.py](counter_string.py)
- [Decoradores en Python: Extiende Funcionalidades de Funciones](https://platzi.com/cursos/python/decoradores-en-python/)
    - Decoradores simple
    [decorators_simple.py](decorators_simple.py)
    [delete_user.py](delete_user.py)
- [Uso de Decoradores Anidados y con Parámetros en Python](https://platzi.com/cursos/python/decoradores-anidados-y-con-parametros/)
    - Decoradores anidados
    [decorators_advanced.py](decorators_advanced.py)
- [Decoradores en Programación Orientada a Objetos en Python](https://platzi.com/cursos/python/uso-de-decoradores-en-clases-y-metodos/)
    - Decoradores en POO
    Solo se crea la clase y se agrega el decorador staticmethod
    [decorators : static.py](decorators/static.py)
    Modfica algun aspecto de la clase con classmethod y se le pasa la clase como parametro
    [decorators : class_method.py](decorators/class_method.py)
    Podemos acceder a un metodo como atributo con property
    [decorators : property.py](decorators/property.py)
- [Uso de Métodos Mágicos en Python](https://platzi.com/cursos/python/metodos-magicos/)
    - Métodos mágicos
    [magic_methods : person.py](magic_methods/person.py)
    [magic_methods : sum_fractions.py](magic_methods/sum_fractions.py)
- [Ejecutar scripts Python con `if __name__ == '__main__'`](https://platzi.com/cursos/python/implementacion-de-if-__name__-__main/)
    - `if __name__ == '__main__'`
    [magic_methods : calculator.py](magic_methods/calculator.py)
- [Metaprogramación en Python: Métodos `__new__` y `__init__`](https://platzi.com/cursos/python/metaprogramacion-en-python/)
    - MultiplerFactory
    [magic_methods : multipler_factory.py](magic_methods/multipler_factory.py)
- [Uso de *args y **kwargs en funciones de Python](https://platzi.com/cursos/python/uso-de-args-y-kwargs/)
    - *args
    Cuando no sabemos cuantos argumentos vamos a recibir en una funcion y llegan como una tupla
    [args_kwargs : args.py](args_kwargs/args.py)
    - **kwargs
    Cuando no sabemos cuantos argumentos nombrados vamos a recibir en una funcion y llegan como un diccionario
    [args_kwargs : kwargs.py](args_kwargs/kwargs.py)
    - usar ambos y el paso de argumentos normales
    [args_kwargs : args_kwargs.py](args_kwargs/args_kwargs.py)
    - desempaquetado de argumentos
    [args_kwargs : unpacking.py](args_kwargs/unpacking.py)
- [Métodos y Atributos Privados y Protegidos en Python](https://platzi.com/cursos/python/metodos-privados-y-protegidos/)
    - Métodos y Atributos Protegidos
    Los metodos y atributos protegidos se indican con un guion bajo al inicio del nombre. Igual quedan accesibles desde fuera de la clase pero se indica que son para uso interno o de subclases.
    [private_protected : protected.py](private_protected/protected.py)
    - Métodos y Atributos Privados
    Los metodos y atributos privados se indican con dos guiones bajos al inicio del nombre. Quedan inaccesibles desde fuera de la clase.
    [private_protected : private.py](private_protected/private.py)
- [Uso de Property en Python: Getter, Setter y Eliminación de Atributos](https://platzi.com/cursos/python/gestion-avanzada-de-propiedades/)
    - Property: Getter, Setter y Deleter
    Uso de property para controlar el acceso a los atributos de una clase.
    [property : employee.py](property/employee.py)
- [Métodos estáticos y de clase en Python](https://platzi.com/cursos/python/metodos-estaticos-y-de-clase-avanzados/)
    - Métodos estáticos
    Acceso a los metodos sin instanciar la clase con staticmethod
    [static_class_methods : order.py](static_class_methods/order.py)
    - Metodos de clase
    Acceso a los metodos de clase sin instanciar la clase con classmethod
    [static_class_methods : person.py](static_class_methods/person.py)
    - Actividad de la clase
    Aplica un descuento si el monto de la orden es mayor a un valor minimo usando classmethod
    [static_class_methods : activity.py](static_class_methods/activity.py)
- [Concurrencia y Paralelismo en Python: Técnicas y Librerías Básicas](https://platzi.com/cursos/python/introduccion-a-la-concurrencia-y-paralelismo/)
    - Concurrencia
    Se simula la ejecucion conurrente de varias tareas usando threading
    [concurrency_asincronia : concurrency.py](concurrency_asincronia/concurrency.py)
    - Paralelismo
    Se simula la ejecucion paralela de varias tareas usando multiprocessing
    [concurrency_asincronia : parallelism.py](concurrency_asincronia/parallelism.py)
- [Concurrencia y Paralelismo en Python: threading y multiprocessing](https://platzi.com/cursos/python/threading-y-multiprocessing-en-python/)
    - Concurrencia con lock
    Se maneja el acceso a un recurso compartido usando locks para evitar condiciones de carrera
    [concurrency_asincronia : concurrency_lock.py](concurrency_asincronia/concurrency_lock.py)
    - Compartir Datos entre Procesos con multiprocessing
    Usamos Queue para que el proceso secundario pueda pasar datos de vuelta al proceso principal.
    [concurrency_asincronia : shared_data_multiprocessing.py](concurrency_asincronia/shared_data_multiprocessing.py)
    - Problemas de Sincronización y Cómo Evitarlos
    Usamos RLock para evitar que múltiples operaciones simultáneas en una cuenta causen bloqueos.
    [concurrency_asincronia : synchronization_problems.py](concurrency_asincronia/synchronization_problems.py)
    - Coordinación de Tareas con multiprocessing.Manager
    Cuando los procesos deben compartir estructuras de datos complejas (como listas o diccionarios), podemos usar un Manager para crear un espacio de memoria compartido entre procesos.
    [concurrency_asincronia : task_coordination.py](concurrency_asincronia/task_coordination.py)
- [Asincronismo en Python con AsyncIO y Corrutinas](https://platzi.com/cursos/python/asincronismo-con-asyncio/)
    - Introduccion a AsyncIO
    Uso basico de async y await para definir y ejecutar corrutinas
    [asyncio : introduction_asyncio.py](asyncio/introduction_asyncio.py)
- [Sincronía y Concurrencia en Python: Teoría y Práctica](https://platzi.com/cursos/python/asincronismo-y-concurrencia/)
    - Sincronía vs Concurrencia
    Comparacion entre ejecucion sincrona y concurrente usando time.sleep para simular tareas que toman tiempo
    [concurrency_asincronia : pedidos_online.py](concurrency_asincronia/pedidos_online.py)
- [Módulos y Paquetes en Python: Reutilización y Organización de Código](https://platzi.com/cursos/python/creacion-de-modulos-en-python/)
    - Módulos y Paquetes
    Creacion y uso de modulos y paquetes en python
    Ayuda a reutilizar y organizar el codigo en proyectos mas grandes.
    Organizacion y mantenibilidad del codigo.
    Cualquier archivo .py es un modulo.
    [modules : reports.py](modules/reports.py)
    [modules : app.py](modules/app.py)
    [modules : app2.py](modules/app2.py)
- [Uso de Paquetes y Subpaquetes en Python con Visual Studio Code](https://platzi.com/cursos/python/gestion-de-paquetes/)
    - Paquetes
    Creacion y uso de paquetes en python
    Facilita la organizacion del codigo en proyectos grandes.
    Evita conflictos de nombres entre modulos.
    [packages : main.py](packages/main.py)
    [packages : __init__.py](packages/ecommerce/__init__.py)
    [packages : inventory.py](packages/ecommerce/inventory.py)
    [packages : sale.py](packages/ecommerce/sale.py)
- [Publicación de Paquetes Python en PyPI](https://platzi.com/cursos/python/publicacion-de-paquetes-en-pypi/)
    - Publicacion en PyPI
    Creacion y publicacion de paquetes en PyPI
    [PyPi](https://pypi.org/) es el repositorio oficial de paquetes de Python.
- [Sistema de Gestión de Reservas en Python Avanzado](https://platzi.com/cursos/python/71751-implementacion-de-un-sistema-completo/)
- Proyecto Final Curso Python Avanzado
    - [proyecto](proyecto)