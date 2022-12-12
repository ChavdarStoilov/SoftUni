from project.computer_types.computer import Computer


class DesktopComputer(Computer):
    PROCESSORS = {"AMD Ryzen 7 5700G": 500,
                  "Intel Core i5-12600K": 600,
                  "Apple M1 Max": 1800
                  }

    MAX_RAM = 128
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
            raise ValueError(f"{processor} is not compatible with desktop computer {self.manufacturer} {self.model}!")

        if ram not in self.VALID_RAMS or ram > self.MAX_RAM:
            raise ValueError(f"{ram}GB RAM is not compatible with desktop computer {self.manufacturer} {self.model}!")

        self.processor = processor
        self.ram = ram
        self.price = (self.VALID_RAMS[ram] * 100) + self.PROCESSORS[processor]

        return f"Created {self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM for {self.price}$."
