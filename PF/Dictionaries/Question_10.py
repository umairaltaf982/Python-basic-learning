# Store Management System
# Create the following dictionary:
# store = {
#     "Laptop": {
#         "price": 120000,
#         "quantity": 5
#     },
#     "Mouse": {
#         "price": 1500,
#         "quantity": 20
#     },
#     "Keyboard": {
#         "price": 3500,
#         "quantity": 10
#     }
# }
# Perform the following tasks:
# Print all products with their price and quantity.
# Update the quantity of Laptop to 8.
# Delete the Mouse product.
# Add a new product:
# Monitor
# Price = 25000
# Quantity = 6
# Print the final dictionary using loops.


store = {
    "Laptop": {
        "price": 120000,
        "quantity": 5
    },
    "Mouse": {
        "price": 1500,
        "quantity": 20
    },
    "Keyboard": {
        "price": 3500,
        "quantity": 10
    }
}

for product, details in store.items():
    print(f"Product: {product} , Price: {details['price']} , Quantity: {details['quantity']}")
store["Laptop"]["quantity"] = 8
del store["Mouse"]
store["Monitor"] = {"price": 25000, "quantity": 6}
for product, details in store.items():
    print(f"Product: {product} , Price: {details['price']} , Quantity: {details['quantity']}")