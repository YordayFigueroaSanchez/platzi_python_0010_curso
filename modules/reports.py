# Genera un informe de ventas para un mes especifico
def generate_sales_report(month: int, sales: int):
    report = f"Informe de Ventas - Mes: {month}\n"
    report += f"Total de Ventas: {sales}\n"
    report += "-------------------------\n"
    report += "Gracias por su preferencia.\n"
    return report

# Genera un informe de gastos para un mes especifico
def generate_expense_report(month: int, expenses: int):
    report = f"Informe de Gastos - Mes: {month}\n"
    report += f"Total de Gastos: {expenses}\n"
    report += "-------------------------\n"
    report += "Revise sus gastos cuidadosamente.\n"
    return report