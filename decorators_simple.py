def payment_decorator(method):
    def wrapper():
        print("1 - Antes")
        method()
        print("3 - Después")
    return wrapper

@payment_decorator
def process_payment():
    print("2 - Processing payment...")

process_payment()