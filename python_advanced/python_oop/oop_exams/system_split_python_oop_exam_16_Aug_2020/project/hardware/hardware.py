class Hardware:

    def __init__(self, name: str, hardware_type: str, capacity: int, memory: int):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []


    def install(self, software):

        if software.memory_consumption <= self.memory and software.capacity_consumption <= self.capacity:
            self.software_components.append(software)

        else:
            raise Exception('Software cannot be installed')


    def uninstall(self, software):

        if software in self.software_components:
            self.software_components.remove(software)