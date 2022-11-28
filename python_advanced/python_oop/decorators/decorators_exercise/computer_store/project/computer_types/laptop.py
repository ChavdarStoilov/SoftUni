from project.computer_types.computer import Computer


class Laptop(Computer):
    PROCESSORS = {
        "AMD Ryzen 9 5950X": 900,
        "Intel Core i9-11900H": 1050,
        "Apple M1 Pro": 1200
    }
    MAX_RAM = 64
    VALID_RAMS = {
        2: 1,
        4: 2,
        8: 3,
        16: 4,
        32: 5,
        64: 6
    }

    def __init__(self, manufacturer: str, model: str):
        super().__init__(manufacturer, model)
        self.processor = None
        self.ram = None
        self.price = 0

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.PROCESSORS:
            raise ValueError(f"{processor}is not compatible with laptop {self.manufacturer} {self.model}!")

        if ram not in self.VALID_RAMS or ram > self.MAX_RAM:
            raise ValueError(f"{ram}GB RAM is not compatible with laptop {self.manufacturer} {self.model}!")

        self.processor = processor
        self.ram = ram
        self.price = (self.VALID_RAMS[ram] * 100) + self.PROCESSORS[processor]

        return f"Created {self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM for {self.price}$."
