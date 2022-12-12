class Hotel:

    def __init__(self, name: str) -> None:
        self.name = name
        self.rooms = []
        self.guests = 0

    def guest(self):
        
        return sum([room.guests for room in self.rooms if room.is_taken])

    def free_rooms(self):

        return [str(room.number) for room in self.rooms if not room.is_taken]

    def taken_rooms(self):

        return [str(room.number) for room in self.rooms if room.is_taken]

    @classmethod
    def from_stars(cls, stars_count: int):
        
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room):
        self.rooms.append(room)

    
    def take_room(self, room_number, people):
        
        for room in self.rooms:
            if room.number == room_number:
                room.take_room(people)


    def free_room(self, room_number):

        for room in self.rooms:
            if room.number == room_number:
                room.free_room()


    def status(self):

        return f"Hotel {self.name} has {self.guest()} total guests\nFree rooms: {', '.join(self.free_rooms())}\nTaken rooms: {', '.join(self.taken_rooms())}"

