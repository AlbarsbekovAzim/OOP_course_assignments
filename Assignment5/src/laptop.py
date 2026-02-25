from src.device import Device


class Laptop(Device):
    def __init__(self, name, price, stock, warranty_period,
                 ram_size, processor_speed):
        super().__init__(name, price, stock, warranty_period)
        self.ram_size = ram_size
        self.processor_speed = processor_speed

    def __str__(self):
        return (super().__str__() +
                f" | RAM: {self.ram_size}GB | CPU: {self.processor_speed}GHz")

    def run_program(self):
        return f"{self.name} is running a program..."

    def use_keyboard(self):
        return f"{self.name} is typing..."