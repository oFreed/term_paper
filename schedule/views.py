from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Player, Stadium, Game


def AllInfo(request):
    return render(request, 'schedule/main.html')


class PlayersList(ListView):
    model = Player
    queryset = Player.objects.all()
    template_name = "schedule/players.html"


class PlayerDetail(DetailView):
    model = Player
    slug_field = "pk"


class StadiumsList(ListView):
    model = Stadium
    queryset = Stadium.objects.all()
    template_name = "schedule/stadiums.html"


class StadiumDetail(DetailView):
    model = Stadium
    slug_field = "pk"


class GamesList(ListView):
    model = Game
    queryset = Game.objects.order_by('date')
    template_name = "schedule/games.html"


class GameDetail(DetailView):
    model = Game
    slug_field = "pk"
