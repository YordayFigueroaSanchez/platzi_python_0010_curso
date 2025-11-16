# importa la función generate_sales_report desde el módulo reports
from reports import generate_sales_report

# Genera un informe de ventas para el mes de enero
month = 1
sales = 1000
report = generate_sales_report(month, sales)
print(report)   