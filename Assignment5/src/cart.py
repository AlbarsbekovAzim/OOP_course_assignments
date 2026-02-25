class Cart:
    def __init__(self):
        self.items = []
        self.total_price = 0

    def add_device(self, device, amount):
        if device.is_available(amount):
            self.items.append((device, amount))
            self.total_price += device.price * amount
            print("Added to cart.")
        else:
            print("Not enough stock!")

    def remove_device(self, device, amount):
        for item in self.items:
            if item[0] == device:
                if item[1] >= amount:
                    self.items.remove(item)
                    self.total_price -= device.price * amount
                    print("Removed from cart.")
                break

    def get_total_price(self):
        return self.total_price

    def print_items(self):
        if not self.items:
            print("Cart is empty.")
            return

        for device, amount in self.items:
            print(f"{device.name} x{amount}")
        print(f"Total: ${self.total_price:.2f}")

    def checkout(self):
        for device, amount in self.items:
            if not device.is_available(amount):
                print("Checkout failed. Not enough stock.")
                return

        for device, amount in self.items:
            device.reduce_stock(amount)

        print("Checkout successful!")
        print(f"Total paid: ${self.total_price:.2f}")
        self.items.clear()
        self.total_price = 0