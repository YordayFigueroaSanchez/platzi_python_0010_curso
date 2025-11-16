import reports

# Genera un informe de ventas para el mes de enero
month = 1
sales = 1000
report = reports.generate_sales_report(month, sales)
print(report)   

# Genera un informe de gastos para el mes de enero
expenses = 500
expense_report = reports.generate_expense_report(month, expenses)
print(expense_report)