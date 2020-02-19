from .models import *
import csv
import os
import re
import threading


def run():

    with open(os.getcwd()+'/ipl/data/Team.csv') as f:
        teams = csv.reader(f)
        next(teams)
        for team in teams:
            _, created = Team.objects.get_or_create(
                Team_Id=team[0], Team_Name=team[1], Team_Short_Code=team[2])
            print("Teams are:-")
            print(_, " --- ", created)

    with open(os.getcwd()+'/ipl/data/Player.csv') as f:
        players = csv.reader(f)
        next(players)
        for player in players:
            _, created = Player.objects.get_or_create(
                Player_Id=player[0],
                Player_Name=player[1],
                DOB=player[2],
                Batting_Hand=player[3],
                Bowling_Skill=player[4],
                Country=player[5],
                Is_Umpire=player[6])
            print("Players are:-")
            print(_, " --- ", created)

    with open(os.getcwd()+'/ipl/data/Season.csv') as f:
        seasons = csv.reader(f)
        next(seasons)
        for season in seasons:
            orange_cap_id = Player.objects.get(Player_Id=season[2])
            purple_cap_id = Player.objects.get(Player_Id=season[3])
            man_of_the_series_id = Player.objects.get(Player_Id=season[4])
            _, created = Season.objects.get_or_create(
                Season_Id=season[0],
                Season_Year=season[1],
                Orange_Cap_Id=orange_cap_id,
                Purple_Cap_Id=purple_cap_id,
                Man_of_the_Series_Id=man_of_the_series_id
            )
            print("Seasons are:-")
            print(_, " --- ", created)

    with open(os.getcwd()+'/ipl/data/Match.csv') as f:
        matches = csv.reader(f)
        next(matches)
        i = 1
        for match in matches:
            team_name_id = Team.objects.get(Team_Id=match[2])
            opponent_team_id = Team.objects.get(Team_Id=match[3])
            season_id = Season.objects.get(Season_Id=match[4])
            toss_winner_id = Team.objects.get(Team_Id=match[6])
            if match[13] != '':
                match_winner_id = Team.objects.get(Team_Id=match[13])
                man_of_the_match_id = Player.objects.get(Player_Id=match[14])
            else:
                match_winner_id = None
                man_of_the_match_id = None

            first_umpire_id = Player.objects.get(Player_Id=match[15])
            second_umpire_id = Player.objects.get(Player_Id=match[16])

            _, created = Match.objects.get_or_create(
                Match_Id=match[0],
                Match_Date=match[1],
                Team_Name_Id=team_name_id,
                Opponent_Team_Id=opponent_team_id,
                Season_Id=season_id,
                Venue_Name=match[5],
                Toss_Winner_Id=toss_winner_id,
                Toss_Decision=match[7],
                Is_Superover=match[8],
                Is_Result=match[9],
                Is_DuckWorthLewis=match[10],
                Win_Type=match[11],
                Won_By=match[12],
                Match_Winner_Id=match_winner_id,
                Man_Of_The_Match_Id=man_of_the_match_id,
                First_Umpire_Id=first_umpire_id,
                Second_Umpire_Id=second_umpire_id,
                City_Name=match[17],
                Host_Country=match[18]
            )
            print(_, " ---- ", created)

    with open(os.getcwd()+'/ipl/data/Ball_by_Ball.csv') as f:
        balls = csv.reader(f)
        next(balls)
        for ball in balls:
            match_id = Match.objects.get(Match_Id=ball[0])
            batting_team_id = Team.objects.get(Team_Id=ball[4])
            bowling_team_id = Team.objects.get(Team_Id=ball[5])
            striker_id = Player.objects.get(Player_Id=ball[6])
            non_striker_id = Player.objects.get(Player_Id=ball[8])
            bowler_id = Player.objects.get(Player_Id=ball[9])
            if re.match("^[0-9]", ball[13]) == None:
                player_dissimal_id = None
            else:
                player_dissimal_id = Player.objects.get(Player_Id=ball[13])

            if re.match("^[0-9]", ball[15]) == None:
                fielder_id = None
            else:
                fielder_id = Player.objects.get(Player_Id=ball[15])

            if re.match("^[0-9]", ball[12]) == None:
                extra_runs = None
            else:
                extra_runs = ball[12]

            if re.match("^[0-9]", ball[10]) == None:
                batsman_scored = None
            else:
                batsman_scored = ball[10]

            _, created = Ball.objects.get_or_create(
                Match_Id=match_id,
                Innings_Id=ball[1],
                Over_Id=ball[2],
                Ball_Id=ball[3],
                Team_Batting_Id=batting_team_id,
                Team_Bowling_Id=bowling_team_id,
                Striker_Id=striker_id,
                Striker_Batting_Position=ball[7],
                Non_Striker_Id=non_striker_id,
                Bowler_Id=bowler_id,
                Batsman_Scored=batsman_scored,
                Extra_Type=ball[11],
                Extra_Runs=extra_runs,
                Player_dissimal_Id=player_dissimal_id,
                Dissimal_Type=ball[14],
                Fielder_Id=fielder_id
            )
            print(_, " ---- ", created)

    with open(os.getcwd()+'/ipl/data/Player_Match.csv') as f:
        PlayerMatchs = csv.reader(f)
        next(PlayerMatchs)

        for player_match in PlayerMatchs:
            match_id = Match.objects.get(Match_Id=player_match[0])
            player_id = Player.objects.get(Player_Id=player_match[1])
            team_id = Team.objects.get(Team_Id=player_match[2])
            _, created = PlayerMatch.objects.get_or_create(
                Match_Id=match_id,
                Player_Id=player_id,
                Team_Id=team_id,
                Is_Keeper=player_match[3],
                Is_Captain=player_match[4]
            )
            print(_, " ---- ", created)
