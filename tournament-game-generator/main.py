def get_number_of_teams():
    num_teams = int(input("Enter the number of teams in the tournament: "))
    while num_teams < 2:
        print("The minimum number of teams is 2, try again.")
        num_teams = int(input("Enter the number of teams in the tournament: "))

    return num_teams

def get_team_names(num_teams):
    team_names = []
    for num in range(num_teams):
        team_name = input(f"Enter the name for team #{num + 1}: ")
        while len(team_name) < 2 or len(team_name.split(" ")) > 2:
            if len(team_name.split(" ")) > 2:
                print("Team names may have at most 2 words, try again.")
            else:
                print("Team names must have at least 2 characters, try again.")
            team_name = input(f"Enter the name for team #{num + 1}: ")
        team_names.append(team_name)

    return team_names

def get_number_of_games_played(num_teams):
    games_played = int(input("Enter the number of games played by each team: "))
    while games_played < num_teams - 1:
        print("Invalid number of games. Each team plays each other at least once in the regular season, try again.")
        games_played = int(input("Enter the number of games played by each team: "))

    return games_played

def get_team_wins(team_names, games_played):
    team_wins = []
    for name in team_names:
        num_wins = int(input(f"Enter the number of wins {name} had: "))
        while num_wins < 0 or num_wins > games_played:
            if num_wins < 0:
                print("The minimum number of wins is 0, try again.")
            else:
                print(f"The maximum number of wins is {games_played}, try again.")
            num_wins = int(input(f"Enter the number of wins {name} had: "))
        team_wins.append((name, num_wins))

    return team_wins

def second_index_sort(item):
    return item[1]

def generate_home_and_away(team_wins):
    sorted_wins = sorted(team_wins, key=second_index_sort)
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