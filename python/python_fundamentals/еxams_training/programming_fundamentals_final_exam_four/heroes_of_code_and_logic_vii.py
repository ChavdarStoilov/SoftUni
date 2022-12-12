count_of_hero = int(input())

party = {}

for _ in range(count_of_hero):
    hero, hp, mp = input().split()

    party[hero] = {"hp": int(hp), "mp": int(mp)}


command = input()

while command != "End":
    action = command.split(" - ")

    hero_mp = party[action[1]]["mp"]
    hero_hp = party[action[1]]["hp"]

    if action[0] == "CastSpell":
        the_hero = action[1]
        needed_mana = int(action[2])
        spell = action[3]
        left_mp = hero_mp - needed_mana

        if left_mp >= 0:
            party[the_hero]["mp"] = left_mp
            print(f"{the_hero} has successfully cast {spell} and now has {left_mp} MP!")
        else:
            print(f"{the_hero} does not have enough MP to cast {spell}!")

    elif action[0] == "TakeDamage":
        the_hero = action[1]
        damage = int(action[2])
        attacker = action[3]
        left_hp = hero_hp - damage

        if left_hp > 0:
            party[the_hero]["hp"] = left_hp
            print(f"{the_hero} was hit for {damage} HP by {attacker} and now has {left_hp} HP left!")
        else:
            party[the_hero].pop("hp")
            party[the_hero].pop("mp")
            party.pop(the_hero)
            print(f"{the_hero} has been killed by {attacker}!")

    elif action[0] == "Recharge":
        the_hero = action[1]
        amount = int(action[2])
        increase_mp = hero_mp + amount
        increased_mp = 0

        if increase_mp <= 200:
            party[the_hero]["mp"] = increase_mp
            increased_mp = amount
        else:
            party[the_hero]["mp"] = 200
            increased_mp = abs(200 - increase_mp)

        print(f"{the_hero} recharged for {increased_mp} MP!")


    elif action[0] == "Heal":
        the_hero = action[1]
        amount = int(action[2])
        increase_hp = hero_hp + amount
        increased_hp = 0

        if increase_hp <= 100:
            party[the_hero]["hp"] = increase_hp
            increased_hp = amount
        else:
            party[the_hero]["hp"] = 100
            increased_hp = abs(100 - hero_hp)

        print(f"{the_hero} healed for {increased_hp} HP!")

    command = input()

for the_party in party.items():
    heroes = the_party[0]
    the_hp = the_party[1]['hp']
    the_mp = the_party[1]['mp']

    print(f"{heroes}\n"
          f" HP: {the_hp}\n"
          f" MP: {the_mp}")
