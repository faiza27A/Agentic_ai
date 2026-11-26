from contextlib import closing
import mysql.connector

# MySQL Database Configuration
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "Littlebear27%",
    "database": "ecommerce"
}

def get_connection():
    """Establishes and returns a connection to MySQL."""
    return mysql.connector.connect(**DB_CONFIG)

def get_order_status(order_id):
    """Fetches order details from MySQL by order_id."""
    query = "SELECT order_id, customer_name, product_name, order_status FROM orders2 WHERE order_id = %s"
    
    with closing(get_connection()) as connection:
        with closing(connection.cursor()) as cursor:
            cursor.execute(query, (order_id,))
            order = cursor.fetchone()
            if not order:
                return "Order not found."
            
            return {
                "order_id": order[0],
                "customer_name": order[1],
                "product_name": order[2],
                "order_status": order[3]
            }

def cancel_order(order_id):
    """Validates order status and cancels the order if eligible."""
    select_query = "SELECT order_status FROM orders2 WHERE order_id = %s"
    update_query = "UPDATE orders2 SET order_status = 'cancelled' WHERE order_id = %s"
    
    with closing(get_connection()) as connection:
        with closing(connection.cursor()) as cursor:
            # Check current order status
            cursor.execute(select_query, (order_id,))
            order = cursor.fetchone()
            
            if not order:
                return "Order not found."
            
            current_status = order[0]
            
            # Validation logic
            if current_status.lower() == "delivered":
                return "Order cannot be cancelled because it is already delivered."
            elif current_status.lower() == "cancelled":
                return "Order is already cancelled."
            
            # Execute update to cancel order
            cursor.execute(update_query, (order_id,))
            connection.commit()
            return "Order cancelled successfully."