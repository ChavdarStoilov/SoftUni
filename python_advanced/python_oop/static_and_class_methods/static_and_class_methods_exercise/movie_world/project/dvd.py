import datetime

class DVD:

    def __init__(self, name: str, id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False


    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int):
        date = date.split('.')
        year, month = date[2], date[1]

        month = datetime.date(int(year), int(month), 1).strftime('%B')

        return cls(name, id, int(year), month, age_restriction)


    def __repr__(self):
        stat = 'rented' if self.is_rented else 'not rented'

        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: {stat}"