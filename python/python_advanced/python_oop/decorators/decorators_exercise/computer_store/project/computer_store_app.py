from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:
    VALID_TYPES_COMPUTER = {
        "Desktop Computer": DesktopComputer,
        "Laptop": Laptop
                            }

    def __init__(self):
        self.warehouse = []
        self.profits = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):

        if type_computer not in self.VALID_TYPES_COMPUTER:
            raise ValueError(f"{type_computer} is not a valid type computer!")

        build = self.VALID_TYPES_COMPUTER[type_computer](manufacturer, model)
        builder = build.configure_computer(processor, ram)
        self.warehouse.append(build)
        return builder

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):

        for computer in self.warehouse:
            if computer.price <= client_budget and wanted_processor == computer.processor and computer.ram >= wanted_ram:
                self.profits += client_budget - computer.price
                self.warehouse.remove(computer)
                return f"{computer} sold for {client_budget}$."

        raise Exception("Sorry, we don't have a computer for you.")
