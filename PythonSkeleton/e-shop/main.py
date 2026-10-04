import time

import product_catalogue
import order_history
import offers

print("[main] Module loaded: product_catalogue")
time.sleep(3)
print("[main] Module loaded: order_history")
time.sleep(3)
print("[main] Module loaded: offers")
time.sleep(3)


def show_menu():
    print("\n=== E-Supermarket CLI ===")
    print("1. List products")
    print("2. Get product details")
    print("3. Search product")
    print("4. List orders")
    print("5. Get order details")
    print("6. Add order")
    print("7. List offers")
    print("8. Get offer details")
    print("9. Apply offer")
    print("0. Exit")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "0":
            print("[main] Exiting the e-supermarket CLI.")
            break

        if choice == "1":
            print("[main] Calling module: product_catalogue")
            time.sleep(3)
            print("[main] Calling function: list_products()")
            time.sleep(3)
            result = product_catalogue.list_products()

        elif choice == "2":
            product_id = input("Enter product ID: ").strip()
            print("[main] Calling module: product_catalogue")
            time.sleep(3)
            print("[main] Calling function: get_product_details()")
            time.sleep(3)
            result = product_catalogue.get_product_details(product_id)

        elif choice == "3":
            keyword = input("Enter product keyword: ").strip()
            print("[main] Calling module: product_catalogue")
            time.sleep(3)
            print("[main] Calling function: search_product()")
            time.sleep(3)
            result = product_catalogue.search_product(keyword)

        elif choice == "4":
            print("[main] Calling module: order_history")
            time.sleep(3)
            print("[main] Calling function: list_orders()")
            time.sleep(3)
            result = order_history.list_orders()

        elif choice == "5":
            order_id = input("Enter order ID: ").strip()
            print("[main] Calling module: order_history")
            time.sleep(3)
            print("[main] Calling function: get_order_details()")
            time.sleep(3)
            result = order_history.get_order_details(order_id)

        elif choice == "6":
            customer_name = input("Enter customer name: ").strip() or "New Customer"
            items = input("Enter order items (comma separated): ").strip()
            items_list = [item.strip() for item in items.split(",") if item.strip()]
            total = float(input("Enter total amount: ") or 0)
            new_order = {
                "customer_name": customer_name,
                "items": items_list,
                "total": total,
                "status": "Placed",
            }
            print("[main] Calling module: order_history")
            time.sleep(3)
            print("[main] Calling function: add_order()")
            time.sleep(3)
            result = order_history.add_order(new_order)

        elif choice == "7":
            print("[main] Calling module: offers")
            time.sleep(3)
            print("[main] Calling function: list_offers()")
            time.sleep(3)
            result = offers.list_offers()

        elif choice == "8":
            offer_code = input("Enter offer code: ").strip()
            print("[main] Calling module: offers")
            time.sleep(3)
            print("[main] Calling function: get_offer_details()")
            time.sleep(3)
            result = offers.get_offer_details(offer_code)

        elif choice == "9":
            offer_code = input("Enter offer code: ").strip()
            total = float(input("Enter cart total: ") or 0)
            print("[main] Calling module: offers")
            time.sleep(3)
            print("[main] Calling function: apply_offer()")
            time.sleep(3)
            result = offers.apply_offer(offer_code, total)

        else:
            print("[main] Invalid choice. Please select a valid option.")
            time.sleep(3)
            continue

        print("\nResult:")
        print(result)
        print("[main] The menu will return in 10 seconds.")
        time.sleep(5)


if __name__ == "__main__":
    main()
