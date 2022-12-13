class Equipment:

    id = 1

    def __init__(self, name: str):
        self.name = name

    @staticmethod
    def get_next_id():
        return Equipment.id


    def __repr__(self) -> str:
        
        return f'Equipment <{self.id}> {self.name}'