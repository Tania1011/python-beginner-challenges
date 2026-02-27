item1 = input("Enter the name of the first item: ")
price1 = float(input("Enter the price of the first item: "))

item2 = input("Enter the name of the second item: ")
price2 = float(input("Enter the price of the second item: "))

item3 = input("Enter the name of the third item: ")
price3 = float(input("Enter the price of the third item: "))

total = price1 + price2 + price3

print("\n--- Shopping Receipt ---")
print(f"Item 1: {item1} - ${price1:.2f}")
print(f"Item 2: {item2} - ${price2:.2f}")
print(f"Item 3: {item3} - ${price3:.2f}")
print("------------------------")
print(f"Total: ${total:.2f}")