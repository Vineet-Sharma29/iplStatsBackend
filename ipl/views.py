from django.http import JsonResponse
from .models import *
from .util import *

# Create your views here.


def index(request):
    stats = {
        'runs_list': get_most_runs(),
        'wickets_list': get_most_wicket(),
        'fielders_list': get_field_assisters(),
        'decision': get_toss_descions(),
        'batting_hand': get_batting_hand(),
        'bowling_hand': get_bowling_hand(),
        'scores': get_scores(),
        'extra_types': get_extra_type(),
        'dissimal_type': get_dissimal_type(),
        'total_superovers': get_n_superover()
    }
    return JsonResponse(stats)
