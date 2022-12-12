card_for_player = input()

list_of_card = card_for_player.split(" ")

team_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


for card in list_of_card:

    team = card[0]
    player = int(card[2:4])
    if team == "A" and player in team_a:
        team_a.remove(player)
    elif team == "B" and player in team_b:
        team_b.remove(player)

    if len(team_a)< 7 or len(team_b) < 7:
        print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
        print("Game was terminated")
        break

else:
    print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")

