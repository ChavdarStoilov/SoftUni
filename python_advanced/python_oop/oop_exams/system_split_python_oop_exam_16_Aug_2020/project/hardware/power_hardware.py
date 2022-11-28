from math import floor
from project.hardware.hardware import Hardware


class PowerHardware(Hardware):


    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name, 'Power', capacity, memory)
        self.capacity = floor(capacity * 0.25)
        self.memory = floor(memory + memory * 0.75)
