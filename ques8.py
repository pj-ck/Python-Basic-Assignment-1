'''
You are given a large dataset in JSON format representing an e-commerce platform's order history, which includes orders from multiple customers. Each order has multiple items, with detailed attributes such as price, quantity, and shipping cost. Additionally, you need to extract specific information, perform calculations like the total cost, apply discounts, and sort the data based on various criteria like the total amount spent by each customer.
The goal is to:
Extract and restructure the data into a tabular format.
Perform calculations such as:
Total order value (price * quantity).
Apply a discount based on the total value of an order (e.g., 10% discount if the order exceeds $100).
Calculate shipping cost based on the number of items ordered (e.g., $5 per item).
Sort the data by the total amount spent by each customer.
Format the output so that it can be easily saved into a CSV file.
'''



import json
import csv


with open('sales.json', 'r') as file:
    data = json.load(file)


def calculate_order_details(order):
    order_id = order.get('order_id', 'N/A')
    customer_name = order.get('customer', {}).get('name', 'Unknown')
    shipping_address = order.get('shipping_address', 'N/A')
    country_code = shipping_address.split(',')[-1].strip() if ',' in shipping_address else 'N/A'

    processed_items = []

    for item in order.get('items', []):
        product_name = item.get('name', 'Unknown')
        price = item.get('price', 0)
        quantity = item.get('quantity', 0)
        
        total_value = price * quantity
        discount = 0.1 * total_value if total_value > 100 else 0
        shipping_cost = 5 * quantity
        final_total = total_value - discount + shipping_cost

        processed_items.append([
            order_id, customer_name, product_name, price, quantity,
            total_value, discount, shipping_cost, final_total,
            shipping_address, country_code
        ])

    return processed_items


all_orders = []
for order in data.get('orders', []):
    all_orders.extend(calculate_order_details(order))


all_orders.sort(key=lambda x: x[8], reverse=True)


header = [
    'Order ID', 'Customer Name', 'Product Name', 'Product Price', 'Quantity Purchased',
    'Total Value', 'Discount', 'Shipping Cost', 'Final Total',
    'Shipping Address', 'Country Code'
]

with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)
    writer.writerows(all_orders)

print("Data processed and saved to 'output.csv'.")
