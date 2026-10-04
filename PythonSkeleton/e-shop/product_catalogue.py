import time

PRODUCTS = [
    {"id": 101, "name": "Organic Apples", "category": "Fruits", "price": 4.50, "stock": 25},
    {"id": 102, "name": "Whole Wheat Bread", "category": "Bakery", "price": 3.20, "stock": 18},
    {"id": 103, "name": "Green Tea", "category": "Beverages", "price": 2.75, "stock": 40},
    {"id": 104, "name": "Rice 5kg", "category": "Groceries", "price": 12.99, "stock": 12},
    {"id": 105, "name": "Tomato Sauce", "category": "Pantry", "price": 2.10, "stock": 30},
]


def list_products():
    print("[product_catalogue] Entered function list_products().")
    time.sleep(3)

    result = {"status": "success", "products": PRODUCTS}

    print("[product_catalogue] Completed list_products() successfully.")
    time.sleep(3)
    return result


def get_product_details(product_id):
    print("[product_catalogue] Entered function get_product_details().")
    time.sleep(3)

    for product in PRODUCTS:
        if str(product["id"]) == str(product_id):
            print(f"[product_catalogue] Product found: {product['name']}.")
            time.sleep(3)
            return {"status": "success", "product": product}

    print(f"[product_catalogue] Status: product with ID '{product_id}' was not found.")
    time.sleep(3)
    return {"status": "not_found", "message": f"Product with ID '{product_id}' was not found."}


def search_product(keyword):
    print("[product_catalogue] Entered function search_product().")
    time.sleep(3)

    search_term = str(keyword).lower().strip()
    matches = []

    for product in PRODUCTS:
        if search_term in product["name"].lower() or search_term in product["category"].lower():
            matches.append(product)

    if matches:
        print(f"[product_catalogue] Search completed. Found {len(matches)} product(s).")
        time.sleep(3)
        return {"status": "success", "results": matches}

    print(f"[product_catalogue] Status: no products matched '{keyword}'.")
    time.sleep(3)
    return {"status": "not_found", "message": f"No products matched '{keyword}'."}
