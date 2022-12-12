from project.pokemon import Pokemon
from project.trainer import Trainer

trainer = Trainer("Ash")
pokemon = Pokemon("Pikachu", 90)
second_pokemon = Pokemon("Charizard", 110)
print(pokemon.pokemon_details())
print(trainer.add_pokemon(pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(pokemon))
print(trainer.release_pokemon('Pikachu'))
print(trainer.release_pokemon('Pikachu'))

print(trainer.add_pokemon(pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
