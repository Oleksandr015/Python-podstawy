import random


class Player:
    def __init__(self, name, age, monthly_salary):
        self.name = name
        self.age = age
        self.monthly_salary = monthly_salary
        self.team = None

    def introduce(self):
        if self.team is None:
            return f'My name is {self.name} I don’t have a team'
        else:
            return f'My {self.name} is name I play for {self.team.name}'

    def __str__(self):
        return self.introduce()

    def __repr__(self):
        return f'Player({self.name}, {self.age}, {self.monthly_salary})'


class Team:
    def __init__(self, name, abbreviation):
        self.name = name
        self.abbreviation = abbreviation
        self.players = []

    def hire_player(self, player):
        self.players.append(player)
        player.team = self

    def fire_player(self, name):
        index = -1
        for i, player in enumerate(self.players):
            if player.name == name:
                index = i
        if index != -1:
            fired_player = self.players.pop(index)
            fired_player.team = None

    def __str__(self):
        return f'{self.name} ({self.abbreviation})'

    def __len__(self):
        return self.size

    @property
    def size(self):
        return len(self.players)

    @property
    def monthly_cost(self):
        return sum([player.monthly_salary for player in self.players])

    @property
    def yearly_cost(self):
        return self.monthly_cost * 12


class Match:
    def __init__(self, host, guest):
        self.host = host
        self.guest = guest
        self.result = None

    def play(self):
        self.result = (random.randint(0, 5), random.randint(0, 5))

    @property
    def goals(self):
        return sum(self.result)

    def __str__(self):
        return f'{self.host} vs {self.guest}'


class TeamStats:
    def __init__(self):
        self.points = 0
        self.wins = 0
        self.draws = 0
        self.loss = 0

    def add_win(self):
        self.points += 3
        self.wins += 1

    def add_loses(self):
        self.loss += 1

    def add_draw(self):
        self.points += 1
        self.draws += 1

    def __str__(self):
        return f'{self.points:>3} {self.draws:>3} {self.loss:>3}'


class League:
    def __init__(self, year, table, matches):
        self.year = year
        self.table = table
        self.matches = matches


def hire_players_in_teams(players, teams):
    for index, player in enumerate(players):
        teams[index % len(teams)].hire_player(player)


def generate_matches(teams):
    matches = []
    for host in teams:
        for guest in teams:
            if host != guest:
                matches.append(Match(host, guest))
    return matches


def build_league(year, teams):
    matches = generate_matches(teams)
    table = {team: TeamStats() for team in teams}


def load_players(path):
    players = []
    with open(path, 'r') as f:
        for line in f:
            line = line.strip()
            attributes = line.split(',')
            players.append(Player(*attributes))
    return players

def load_teams(path):
    teams = []
    with open(path, 'r') as f:
        for line in f:
            line = line.strip()
            attributes = line.split(',')
            teams.append(Team(attributes[1], attributes[0]))
    return teams


if __name__ == '__main__':
    player_1 = Player('Piotr', 25, 15000)
    #player_2 = Player('Eva', 23, 12000)
    #print(player_1.introduce())
    #print(player_1)
    #print(repr(player_1))
    # print()
    team_1 = Team('Liverpool FC', 'LFC')
    team_1.hire_player(player_1)
    print('After Piotr Hired')
    print(team_1.players)
    team_1.fire_player('Piotr')
    print('After Piotr Fired')
    print(team_1.players)

    player_1 = Player('Piotr', 25, 15000)
    player_2 = Player('Eva', 23, 12000)

    team_1 = Team('Liverpool FC', 'LFC')
    team_2 = Team('Chelsui FC', 'CHE')

    match_1 = Match(team_1, team_2)
    match_1.play()
    print(match_1.result)
    print(match_1)

    ts = TeamStats()
    ts.add_draw()
    ts.add_win()
    print(ts)

    players = load_players('players.txt')
    teams = load_teams('teams.txt')

    hire_players_in_teams(players, teams)
    #print(teams[0].players)
    #league = build_league(2019, teams)
    #league.play_season()
    #print(league)
    print(generate_matches(teams))
