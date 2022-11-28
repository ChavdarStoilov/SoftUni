from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        valid_horse_types = {
            'Appaloosa': Appaloosa,
            'Thoroughbred': Thoroughbred
        }
        for horse in self.horses:
            if horse.name == horse_name:
                raise Exception(f'Horse {horse_name} has been already added!')

        if horse_type in valid_horse_types:
            self.horses.append(valid_horse_types[horse_type](horse_name, horse_speed))
            return f'{horse_type} horse {horse_name} is added.'

    def add_jockey(self, jockey_name: str, age: int):

        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                raise Exception(f'Jockey {jockey_name} has been already added!')

        self.jockeys.append(Jockey(jockey_name, age))
        return f'Jockey {jockey_name} is added.'

    def create_horse_race(self, race_type: str):

        for race in self.horse_races:
            if race_type == race.race_type:
                raise Exception(f'Race {race_type} has been already created!')

        self.horse_races.append(HorseRace(race_type))
        return f'Race {race_type} is created.'

    def get_horse_instance(self, horse_type):
        for horse in self.horses:
            if horse.__class__.__name__ == horse_type:
                if not horse.is_taken:
                    return horse

        raise Exception(f'Horse breed {horse_type} could not be found!')

    def get_jockey_instance(self, jockey_name):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                return jockey

        raise Exception(f'Jockey {jockey_name} could not be found!')

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        horse = self.get_horse_instance(horse_type)
        jockey = self.get_jockey_instance(jockey_name)

        if jockey.horse:
            return f'Jockey {jockey_name} already has a horse.'

        horse.is_taken = True
        jockey.horse = horse
        return f'Jockey {jockey_name} will ride the horse {horse.name}.'


    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        jockey = self.get_jockey_instance(jockey_name)

        if jockey not in self.jockeys:
            raise Exception(f'Jockey {jockey_name} could not be found!')

        if jockey in self.jockeys and not jockey.horse:
            raise Exception(f'Jockey {jockey_name} cannot race without a horse!')

        for races in self.horse_races:
            if jockey in races.jockeys:
                return f'Jockey {jockey_name} has been already added to the {race_type} race.'

            if race_type not in races.race_type:
                raise Exception(f'Race {race_type} could not be found!')

            races.jockeys.append(jockey)
            return f'Jockey {jockey_name} added to the {race_type} race.'

    def start_horse_race(self, race_type: str):

        for race in self.horse_races:
            if race.race_type == race_type:
                if len(race.jockeys) < 2:
                    raise Exception(f'Horse race {race_type} needs at least two participants!')

                jockeys = {jockey.horse.speed: [jockey.name, jockey.horse.name] for jockey in race.jockeys}
                ranked = sorted(jockeys.items(), key=lambda x: x[0], reverse=True)

                highest_speed, names = ranked[0]
                jockey_name = names[0]
                horse_name = names[1]


                return f'The winner of the {race_type} race, with a speed of {highest_speed}km/h is {jockey_name}! Winner\'s horse: {horse_name}.'

        raise Exception(f'Race {race_type} could not be found!')