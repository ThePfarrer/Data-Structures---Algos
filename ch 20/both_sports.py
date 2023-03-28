def players_two_sports(arr1, arr2):
    output = []
    hash_map = {}

    for player in arr1:
        full_name = player["first_name"] + " " + player["last_name"]
        hash_map[full_name] = True

    for player in arr2:
        full_name = player["first_name"] + " " + player["last_name"]
        if hash_map.get(full_name):
            output.append(full_name)

    return output


basketball_players = [
    {"first_name": "Jill", "last_name": "Huang", "team": "Gators"},
    {"first_name": "Janko", "last_name": "Barton", "team": "Sharks"},
    {"first_name": "Wanda", "last_name": "Vakulskas", "team": "Sharks"},
    {"first_name": "Jill", "last_name": "Moloney", "team": "Gators"},
    {"first_name": "Luuk", "last_name": "Watkins", "team": "Gators"},
]

football_players = [
    {"first_name": "Hanzla", "last_name": "Radosti", "team": "32ers"},
    {"first_name": "Tina", "last_name": "Watkins", "team": "Barleycorns"},
    {"first_name": "Alex", "last_name": "Patel", "team": "32ers"},
    {"first_name": "Jill", "last_name": "Huang", "team": "Barleycorns"},
    {"first_name": "Wanda", "last_name": "Vakulskas", "team": "Barleycorns"},
]

print(players_two_sports(basketball_players, football_players))
