# importar las funciones de los modulos dentro del paquete ecommerce
from ecommerce.inventory import add_product, remove_product
from ecommerce.sale import process_sale

# usar las funciones importadas
add_product("Laptop", 10)
process_sale("Laptop", 2)
remove_product("Laptop")