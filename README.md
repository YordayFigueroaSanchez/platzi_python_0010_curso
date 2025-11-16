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
