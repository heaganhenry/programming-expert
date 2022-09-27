def get_number_of_teams():
    while True:
        num_teams = int(input("Enter the number of teams in the tournament: "))
        if num_teams >= 2:
            break
        print("The minimum number of teams is 2, try again.")

    return num_teams

def get_team_names(num_teams):
    team_names = []

    for num in range(num_teams):
        while True:
            team_name = input(f"Enter the name for team #{num + 1}: ")
            if len(team_name.split(" ")) > 2:
                print("Team names may have at most 2 words, try again.")
            elif len(team_name) < 2:
                print("Team names must have at least 2 characters, try again.")
            else:
                break

        team_names.append(team_name)

    return team_names

def get_number_of_games_played(num_teams):
    while True:
        games_played = int(input("Enter the number of games played by each team: "))
        if games_played >= num_teams - 1:
            break
        print("Invalid number of games. Each team plays each other at least once in the regular season, try again.")

    return games_played

def get_team_wins(team_names, games_played):
    team_wins = []

    for team in team_names:
        while True:
            wins = int(input(f"Enter the number of wins {team} had: "))
            if wins < 0:
                print("The minimum number of wins is 0, try again.")
            elif wins > games_played:
                print(f"The maximum number of wins is {games_played}, try again.")
            else:
                break

        team_wins.append((team, wins))

    return team_wins

def get_second_item(item):
    return item[1]

def generate_home_and_away(team_wins):
    sorted_wins = sorted(team_wins, key=get_second_item)
    for idx in range(num_teams // 2):
        home_team = sorted_wins[idx]
        away_team = sorted_wins[-1 - idx]
        print(f"Home: {home_team[0]} VS Away: {away_team[0]}")

num_teams = get_number_of_teams()
team_names = get_team_names(num_teams)
games_played = get_number_of_games_played(num_teams)
team_wins = get_team_wins(team_names, games_played)

print("Generating the games to be played in the first round of the tournament...")
generate_home_and_away(team_wins)