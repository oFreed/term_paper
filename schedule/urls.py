from django.urls import path
from .views import PlayersList,GamesList,StadiumsList, AllInfo, PlayerDetail, GameDetail, StadiumDetail

app_name = 'player'
urlpatterns = [
    path('', AllInfo, name='players'),
    path('players/', PlayersList.as_view(), name='players'),
    path('players/<pk>', PlayerDetail.as_view(), name='player'),
    path('games/', GamesList.as_view(), name='games'),
    path('games/<pk>', GameDetail.as_view(), name='game'),
    path('stadiums/', StadiumsList.as_view(), name='stadiums'),
    path('stadiums/<pk>', StadiumDetail.as_view(), name='stadium'),
]
