from project.delicacies.stolen import Stolen
from project.delicacies.gingerbread import Gingerbread
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth

class ChristmasPastryShopApp:
    __VALID_DELICACY = {"Gingerbread": Gingerbread,
                        "Stolen": Stolen}

    __VALID_BOOTH = {"Open Booth": OpenBooth,
                     "Private Booth": PrivateBooth}


    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0.0


    def add_delicacy(self, type_delicacy: str, name: str, price: float):

        if type_delicacy not in self.__VALID_DELICACY.keys():
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        for delicacy in self.delicacies:
            if delicacy.name == name:
                raise Exception(f"{name} already exists!")


        valid_delicacy = self.__VALID_DELICACY[type_delicacy](name, price)
        self.delicacies.append(valid_delicacy)

        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):

        if type_booth not in self.__VALID_BOOTH.keys():
            raise Exception(f"{type_booth} is not a valid booth!")

        for booth in self.booths:
            if booth.booth_number == booth_number:
                raise Exception(f"Booth number {booth_number} already exists!")


        valid_booth = self.__VALID_BOOTH[type_booth](booth_number, capacity)
        self.booths.append(valid_booth)

        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):

        for booths in self.booths:
            if booths.capacity >= number_of_people:
                booths.reserve(number_of_people)
                return f"Booth {booths.booth_number} has been reserved for {number_of_people} people."

        raise Exception(f"No available booth for {number_of_people} people!")

    def order_delicacy(self, booth_number: int, delicacy_name: str):

        for booth in self.booths:
            if booth.booth_number == booth_number:
                for delicacy in self.delicacies:
                    if delicacy.name == delicacy_name:
                        booth.delicacy_orders.append(delicacy)
                        return f"Booth {booth_number} ordered {delicacy_name}."

                raise Exception(f"No {delicacy_name} in the pastry shop!")

        raise Exception(f"Could not find booth {booth_number}!")

    def leave_booth(self, booth_number: int):
        bill = 0

        for booth in self.booths:
            if booth.booth_number == booth_number:
                bill += booth.price_for_reservation

                for orders in booth.delicacy_orders:
                    bill += orders.price

                booth.delicacy_orders = []
                booth.price_for_reservation = 0
                booth.is_reserved = False

        self.income += bill
        return f"Booth {booth_number}:\n" \
               f"Bill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."
