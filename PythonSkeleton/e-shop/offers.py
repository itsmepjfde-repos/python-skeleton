import time

OFFERS = [
    {"code": "SAVE10", "title": "10% Off", "discount_type": "percentage", "value": 10, "minimum_amount": 25.0},
    {"code": "FREESHIP", "title": "Free Shipping", "discount_type": "shipping", "value": 0, "minimum_amount": 30.0},
    {"code": "BUNDLE5", "title": "5% Bundle Discount", "discount_type": "percentage", "value": 5, "minimum_amount": 50.0},
]


def list_offers():
    print("[offers] Entered function list_offers().")
    time.sleep(3)

    result = {"status": "success", "offers": OFFERS}

    print("[offers] Completed list_offers() successfully.")
    time.sleep(3)
    return result


def get_offer_details(offer_code):
    print("[offers] Entered function get_offer_details().")
    time.sleep(3)

    normalized_code = str(offer_code).upper().strip()

    for offer in OFFERS:
        if offer["code"] == normalized_code:
            print(f"[offers] Offer found: {offer['title']}.")
            time.sleep(3)
            return {"status": "success", "offer": offer}

    print(f"[offers] Status: offer code '{offer_code}' is invalid.")
    time.sleep(3)
    return {"status": "invalid", "message": f"Offer code '{offer_code}' is invalid."}


def apply_offer(offer_code, cart_total):
    print("[offers] Entered function apply_offer().")
    time.sleep(3)

    normalized_code = str(offer_code).upper().strip()
    cart_value = float(cart_total)

    for offer in OFFERS:
        if offer["code"] == normalized_code:
            if cart_value < offer["minimum_amount"]:
                print(f"[offers] Status: offer '{offer_code}' is not valid for a cart total of {cart_value}.")
                time.sleep(3)
                return {
                    "status": "not_eligible",
                    "message": f"Offer '{offer_code}' requires a minimum cart total of {offer['minimum_amount']}.",
                    "discount_applied": 0.0,
                }

            if offer["discount_type"] == "percentage":
                discount = (cart_value * offer["value"]) / 100
            else:
                discount = 0.0

            final_total = cart_value - discount
            print(f"[offers] Offer '{offer_code}' applied successfully.")
            time.sleep(3)
            return {
                "status": "success",
                "message": f"Offer '{offer_code}' applied successfully.",
                "discount_applied": round(discount, 2),
                "final_total": round(final_total, 2),
            }

    print(f"[offers] Status: offer code '{offer_code}' is invalid.")
    time.sleep(3)
    return {"status": "invalid", "message": f"Offer code '{offer_code}' is invalid."}
