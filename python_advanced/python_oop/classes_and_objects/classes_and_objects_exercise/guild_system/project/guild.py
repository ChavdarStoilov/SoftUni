class Guild:

    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player):

        if player.guild == 'Unaffiliated':
            player.guild = self.name
            self.players.append(player)
            return f'Welcome player {player.name} to the guild {self.name}'
        elif player.guild == self.name:
            return f'Player {player.name} is already in the guild.'

        return f'Player {player.name} is in another guild.'



    def kick_player(self, player):

        for hero in self.players:
            if player == hero.name:
                self.players.remove(hero)
                hero.guild = 'Unaffiliated'
                return f'Player {player} has been removed from the guild.'

        return f'Player {player} is not in the guild.'

    def guild_info(self):
        heroes = '\n'.join([hero.player_info() for hero in self.players])
        return f'Guild: {self.name}\n{heroes}'
