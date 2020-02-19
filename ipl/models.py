from django.db import models


# Team Metadata
class Team(models.Model):
    Team_Id = models.IntegerField(primary_key=True)
    Team_Name = models.CharField(max_length=50)
    Team_Short_Code = models.CharField(max_length=5)


# Player metadata
class Player(models.Model):
    Player_Id = models.IntegerField(primary_key=True)
    Player_Name = models.CharField(max_length=50)
    DOB = models.CharField(max_length=15)
    Batting_Hand = models.CharField(max_length=20)
    Bowling_Skill = models.CharField(max_length=50)
    Country = models.CharField(max_length=30)
    Is_Umpire = models.IntegerField()


# Season Metadata
class Season(models.Model):
    Season_Id = models.IntegerField(primary_key=True)
    Season_Year = models.IntegerField()
    Orange_Cap_Id = models.ForeignKey(
        Player, on_delete=models.CASCADE, related_name="orange_cap_id")
    Purple_Cap_Id = models.ForeignKey(
        Player, on_delete=models.CASCADE, related_name="purple_cap_id")
    Man_of_the_Series_Id = models.ForeignKey(
        Player, on_delete=models.CASCADE, related_name="man_of_the_series_id")


# Match Metadata
class Match(models.Model):
    Match_Id = models.IntegerField(primary_key=True)
    Match_Date = models.CharField(max_length=15)
    Team_Name_Id = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name="Team_Name_Id")
    Opponent_Team_Id = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name="Opponent_Team_Id")
    Season_Id = models.ForeignKey(
        Season, on_delete=models.CASCADE, related_name="%(class)s_Season_Id")
    Venue_Name = models.CharField(max_length=60)
    Toss_Winner_Id = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name="Toss_Winner_Id")
    Toss_Decision = models.CharField(max_length=10)
    Is_Superover = models.IntegerField()
    Is_Result = models.IntegerField()
    Is_DuckWorthLewis = models.IntegerField()
    Win_Type = models.CharField(max_length=10)
    Won_By = models.CharField(max_length=6, blank=True, null=True)
    Match_Winner_Id = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name="Match_Winner_Id", blank=True, null=True)
    Man_Of_The_Match_Id = models.ForeignKey(
        Player, on_delete=models.CASCADE, related_name="Man_Of_The_Match_Id", blank=True, null=True)
    First_Umpire_Id = models.ForeignKey(
        Player, on_delete=models.CASCADE, related_name="First_Umpire_Id")
    Second_Umpire_Id = models.ForeignKey(
        Player, on_delete=models.CASCADE, related_name="Second_Umpire_Id")
    City_Name = models.CharField(max_length=50)
    Host_Country = models.CharField(max_length=50)


# Includes Ball by Ball details of each match
class Ball(models.Model):
    Match_Id = models.ForeignKey(
        Match, on_delete=models.CASCADE, related_name="%(class)s_Match_Id")
    Innings_Id = models.IntegerField()
    Over_Id = models.IntegerField()
    Ball_Id = models.IntegerField()
    Team_Batting_Id = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name="Team_Batting_Id")
    Team_Bowling_Id = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name="Team_Bowling_Id")
    Striker_Id = models.ForeignKey(
        Player, on_delete=models.CASCADE, related_name="Striker_Id")
    Striker_Batting_Position = models.IntegerField()
    Non_Striker_Id = models.ForeignKey(
        Player, on_delete=models.CASCADE, related_name="Non_Striker_Id")
    Bowler_Id = models.ForeignKey(
        Player, on_delete=models.CASCADE, related_name="Bowler_Id")
    Batsman_Scored = models.IntegerField(blank=True, null=True)
    Extra_Type = models.CharField(blank=True, null=True, max_length=15)
    Extra_Runs = models.IntegerField(blank=True, null=True)
    Player_dissimal_Id = models.ForeignKey(
        Player, on_delete=models.CASCADE, null=True, related_name="Player_dissimal_Id")
    Dissimal_Type = models.CharField(blank=True, null=True, max_length=25)
    Fielder_Id = models.ForeignKey(
        Player, on_delete=models.CASCADE, blank=True, null=True, related_name="Fielder_Id")


# Includes every player who took part in the match
class PlayerMatch(models.Model):
    Match_Id = models.ForeignKey(
        Match, on_delete=models.CASCADE, related_name="%(class)s_Match_Id")
    Player_Id = models.ForeignKey(
        Player, on_delete=models.CASCADE, related_name="%(class)s_Player_Id")
    Team_Id = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name="%(class)s_Team_Id")
    Is_Keeper = models.IntegerField()
    Is_Captain = models.IntegerField()
