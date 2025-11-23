class MultiplerFactory:

    def __new__(cls, factor: int):
        if factor <= 0:
            raise ValueError("El factor debe ser un entero positivo.")
        print(f"Creando una instancia de MultiplerFactory con factor {factor}")
        return super(MultiplerFactory, cls).__new__(cls)

    def __init__(self, factor: int):
        print(f"Inicializando MultiplerFactory con factor {factor}")
        self.factor = factor

    def __call__(self, value: int) -> int:
        return self.factor * value
    
if __name__ == "__main__":
    doubler = MultiplerFactory(2)
    tripler = MultiplerFactory(3)

    print(doubler(5))  # Output: 10
    print(tripler(5))  # Output: 15