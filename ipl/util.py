from .models import *
from django.db.models import Sum, Count, Q, F, ExpressionWrapper, BooleanField


def get_most_runs():
    runs_list = Ball.objects.values(
        'Striker_Id').annotate(runs=Sum('Batsman_Scored'))
    sorted_runs_list = sorted(runs_list, key=lambda i: i['runs'], reverse=True)
    top_10_runs = sorted_runs_list[:10]
    result = []
    for run in top_10_runs:
        result.append(
            {
                'label': Player.objects.get(pk=run['Striker_Id']).Player_Name,
                'value': run['runs']
            }
        )
    return result


def get_most_wicket():
    wicket_list = Ball.objects.values('Bowler_Id').annotate(
        wickets=Count('Player_dissimal_Id'))
    sorted_wicket_list = sorted(
        wicket_list, key=lambda i: i['wickets'], reverse=True)
    top_10_wickets = sorted_wicket_list[:10]
    result = []
    for wicket in top_10_wickets:
        result.append(
            {
                'label': Player.objects.get(pk=wicket['Bowler_Id']).Player_Name,
                'value': wicket['wickets']
            }
        )
    return result


def get_field_assisters():
    fielders = Ball.objects.values(
        'Fielder_Id').annotate(cnt=Count('Dissimal_Type'))
    sorted_fielders = sorted(fielders, key=lambda i: i['cnt'], reverse=True)
    top_10_fielders = sorted_fielders[1:11]
    result = []
    for field in top_10_fielders:
        result.append(
            {
                'label': Player.objects.get(pk=field['Fielder_Id']).Player_Name,
                'value': field['cnt']
            }
        )
    return result

# def get_most_sixes():
#     sixes_list = Ball.objects.values('Striker_Id').annotate(
#         sixes=Count('Player_dissimal_Id'))


def get_toss_descions():
    toss_decisions = Match.objects.values('Toss_Decision').annotate(
        flag=ExpressionWrapper(Q(Match_Winner_Id=F('Toss_Winner_Id')), output_field=BooleanField()))
    decision = {'bat': 0, 'field': 0}
    for i in toss_decisions:
        if i['flag']:
            decision[i['Toss_Decision']] = decision[i['Toss_Decision']] + 1
    return decision


def get_batting_hand():
    batting_hand = list(Player.objects.values(
        'Batting_Hand').annotate(cnt=Count('Batting_Hand')))

    result = {}

    for i in batting_hand:
        result[i['Batting_Hand']] = i['cnt']

    del result["NULL"]

    return result


def get_bowling_hand():
    bowling_hand = list(Player.objects.values(
        'Bowling_Skill').annotate(cnt=Count('Bowling_Skill')))

    result = {}

    for i in bowling_hand:
        result[i['Bowling_Skill']] = i['cnt']

    del result["NULL"]

    return result


def get_scores():
    scores = Ball.objects.values('Batsman_Scored').annotate(
        cnt=Count('Batsman_Scored'))

    result = {}

    for i in scores:
        result["score_"+str(i['Batsman_Scored'])] = i['cnt']

    del result["score_None"]

    return result


def get_extra_type():
    extra_types = Ball.objects.values(
        'Extra_Type').annotate(cnt=Count('Extra_Type'))

    result = {}

    for i in extra_types:
        result[i['Extra_Type']] = i['cnt']

    del result[" "]

    return result


def get_dissimal_type():
    dissimal_type = Ball.objects.values(
        'Dissimal_Type').annotate(cnt=Count('Dissimal_Type'))

    result = {}

    for i in dissimal_type:
        result[i['Dissimal_Type']] = i['cnt']

    del result[" "]

    return result


def get_n_superover():
    n_superover = Match.objects.values(
        'Is_Superover').annotate(cnt=Count('Is_Superover'))
    result = {}

    for i in n_superover:
        result[i["Is_Superover"]] = i['cnt']

    del result[0]

    return result[1]
