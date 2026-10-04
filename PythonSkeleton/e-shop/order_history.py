import time

ORDERS = [
    {"id": 1, "customer_name": "Aisha", "items": ["Organic Apples", "Green Tea"], "total": 7.25, "status": "Delivered"},
    {"id": 2, "customer_name": "Daniel", "items": ["Rice 5kg", "Tomato Sauce"], "total": 15.09, "status": "Processing"},
    {"id": 3, "customer_name": "Priya", "items": ["Whole Wheat Bread"], "total": 3.20, "status": "Delivered"},
]


def list_orders():
    print("[order_history] Entered function list_orders().")
    time.sleep(3)

    result = {"status": "success", "orders": ORDERS}

    print("[order_history] Completed list_orders() successfully.")
    time.sleep(3)
    return result


def get_order_details(order_id):
    print("[order_history] Entered function get_order_details().")
    time.sleep(3)

    for order in ORDERS:
        if str(order["id"]) == str(order_id):
            print(f"[order_history] Order found: Order #{order['id']}.")
            time.sleep(3)
            return {"status": "success", "order": order}

    print(f"[order_history] Status: order with ID '{order_id}' was not found.")
    time.sleep(3)
    return {"status": "not_found", "message": f"Order with ID '{order_id}' was not found."}


def add_order(new_order):
    print("[order_history] Entered function add_order().")
    time.sleep(3)

    if not isinstance(new_order, dict):
        print("[order_history] Status: invalid order data provided.")
        time.sleep(3)
        return {"status": "invalid", "message": "Order data must be a dictionary."}

    new_id = max(order["id"] for order in ORDERS) + 1
    order = {
        "id": new_id,
        "customer_name": new_order.get("customer_name", "Unknown Customer"),
        "items": new_order.get("items", []),
        "total": new_order.get("total", 0.0),
        "status": new_order.get("status", "Placed"),
    }
    ORDERS.append(order)

    print(f"[order_history] New order added successfully: Order #{new_id}.")
    time.sleep(3)
    return {"status": "success", "message": "Order added successfully.", "order": order}
