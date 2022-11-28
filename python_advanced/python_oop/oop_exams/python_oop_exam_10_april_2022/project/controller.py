class Controller:

    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *players):
        added_players = []
        for player in players:
            if player not in self.players:
                self.players.append(player)
                added_players.append(player.name)

        return f'Successfully added: {", ".join(added_players)}'

    def add_supply(self, *supplies):
        self.supplies.extend(supplies)

    def get_player_instance(self, player):
        for players in self.players:
            if player == players.name:
                return players

    def get_supply_instance(self, supply):
        for idx in range(len(self.supplies) - 1, -1, -1):
            supplies = self.supplies[idx]
            if supply == supplies.__class__.__name__:
                return self.supplies.pop(idx)

    def sustain(self, player_name: str, sustenance_type: str):
        player = self.get_player_instance(player_name)
        supply = self.get_supply_instance(sustenance_type)

        if player is None:
            return

        if sustenance_type != 'Food' and sustenance_type != 'Drink':
            return

        if supply is None:
            raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

        if not player.need_sustenance:
            return f"{player.name} have enough stamina."

        player.stamina = min(player.stamina + supply.energy, 100)
        return f'{player.name} sustained successfully with {supply.name}.'

    @staticmethod
    def check_players_stamina(player_one, player_two):
        result = ''

        if player_one.stamina == 0:
            result += f'Player {player_one.name} does not have enough stamina.'

        if player_two.stamina == 0:
            result += f'\nPlayer {player_two.name} does not have enough stamina.'

        return result.strip()

    @staticmethod
    def attack(attacker, enemy):
        enemy.stamina = max(enemy.stamina - attacker.stamina / 2, 0)

        return enemy.stamina == 0

    def duel(self, first_player_name: str, second_player_name: str):
        first_player = self.get_player_instance(first_player_name)
        second_player = self.get_player_instance(second_player_name)
        stamina_checker = self.check_players_stamina(first_player, second_player)

        if stamina_checker:
            return stamina_checker

        if second_player.stamina < first_player.stamina:
            first_player, second_player = second_player, first_player

        if self.attack(first_player, second_player):
            return f'Winner: {first_player.name}'

        if self.attack(second_player, first_player):
            return f'Winner: {second_player.name}'

        winner = first_player if first_player.stamina > second_player.stamina else second_player
        return f'Winner: {winner.name}'

    def next_day(self):

        for player in self.players:
            player.stamina = max(player.stamina - player.age * 2, 0)
            self.sustain(player.name, 'Food')
            self.sustain(player.name, 'Drink')

    def __str__(self):

        return '\n'.join([str(p) for p in self.players]) + '\n' + '\n'.join([s.details() for s in self.supplies])
