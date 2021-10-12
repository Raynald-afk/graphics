def team_player_summary(team_dic):
    """
    This function calculates the teams and their points


    :param team_dic:
    :return:
    """
    score = 0
    team = ""
    for high_score_team in team_dic:
       if team_dic[high_score_team] > score:
           score = team_dic[high_score_team]
           team = high_score_team
    print(team, "won!")
    print(team,"scored",score,"points.")
    for teams in team_dic:
        if teams != team:
            print(teams,"scored",team_dic[teams], "points.")
def player():
    """
    this function calculate for the player
    which scored first and last
    the file parameter is the read_in log
    :return:
    """
    file = open("log","r")
    first_player = file.readline().split()
    print(first_player[1],"scored first.")

    for last_player in file:
        last_line =last_player.split()
    print(last_line[1],"scored last.")
def main():
    team_dic = {}
    file = open("log","r")
        # loading in the text file to be processed
    for info in file:
        line = info.strip().split()
        if line[0] not in team_dic:

            team_dic[line[0]] = 0
        team_dic[line[0]] +=int(line[2])
    team_player_summary(team_dic)
    player()

main()