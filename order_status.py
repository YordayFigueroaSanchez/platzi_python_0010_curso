from enum import Enum

class OrderStatus(Enum):
    PENDING = 1 #Pending
    SHIPPED = 2 #Shipped
    DELIVERED = 3 #Delivered
    CANCELED = 4 #Canceled

def get_order_status_message(status):
    if status == OrderStatus.PENDING:
        return "Your order is pending."
    elif status == OrderStatus.SHIPPED:
        return "Your order has been shipped."
    elif status == OrderStatus.DELIVERED:
        return "Your order has been delivered."
    elif status == OrderStatus.CANCELED:
        return "Your order has been canceled."
    else:
        return "Unknown order status."
    
print(get_order_status_message(OrderStatus.SHIPPED))