# 7-8. Deli

sandwich_orders = [
    "tuna",
    "turkey",
    "ham and cheese",
    "chicken",
    "roast beef"
]

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"I made your {current_sandwich} sandwich.")

    finished_sandwiches.append(current_sandwich)

print("\nFinished sandwiches:")