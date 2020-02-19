from .models import *
from django.db.models import Sum, Count, Q, F, ExpressionWrapper, BooleanField


def get_most_runs():
    runs_list = Ball.objects.values(
        'Striker_Id').annotate(runs=Sum('Batsman_Scored'))
    sorted_runs_list = sorted(runs_list, key=lambda i: i['runs'], reverse=True)
    return sorted_runs_list[:10]


def get_most_wicket():
    wicket_list = Ball.objects.values('Bowler_Id').annotate(
        wickets=Count('Player_dissimal_Id'))
    sorted_wicket_list = sorted(
        wicket_list, key=lambda i: i['runs'], reverse=True)
    return sorted_wicket_list[:10]


# def get_most_sixes():
#     sixes_list = Ball.objects.values('Striker_Id').annotate(
#         sixes=Count('Player_dissimal_Id'))

def get_toss_descions():
    toss_decisions = v = Match.objects.values('Toss_Decision').annotate(
        flg=ExpressionWrapper(Q(Match_Winner_Id=F('Toss_Winner_Id')), output_field=BooleanField()))
