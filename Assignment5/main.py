from src.smartphone import Smartphone
from src.laptop import Laptop
from src.tablet import Tablet
from src.cart import Cart

devices = []

# Create 20 devices
for i in range(1, 8):
    devices.append(Smartphone(f"Phone{i}", 500+i*10, 10+i, 24, 6.5, 20))
    devices.append(Laptop(f"Laptop{i}", 1000+i*20, 5+i, 36, 16, 3.2))
    devices.append(Tablet(f"Tablet{i}", 300+i*15, 8+i, 12, "1920x1080", 450))

cart = Cart()

while True:
    print("\n1. Show Devices")
    print("2. Show Cart")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        for idx, device in enumerate(devices):
            print(f"{idx}. {device}")

        index = int(input("Select device number: "))
        amount = int(input("Quantity: "))
        cart.add_device(devices[index], amount)

    elif choice == "2":
        cart.print_items()

    elif choice == "3":
        break