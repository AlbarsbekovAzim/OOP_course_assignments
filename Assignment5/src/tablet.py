from src.device import Device


class Tablet(Device):
    def __init__(self, name, price, stock, warranty_period,
                 screen_resolution, weight):
        super().__init__(name, price, stock, warranty_period)
        self.screen_resolution = screen_resolution
        self.weight = weight

    def __str__(self):
        return (super().__str__() +
                f" | Resolution: {self.screen_resolution} | Weight: {self.weight}g")

    def browse_internet(self):
        return f"{self.name} is browsing..."

    def use_touchscreen(self):
        return f"{self.name} touchscreen in use..."