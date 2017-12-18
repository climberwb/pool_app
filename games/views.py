from django.shortcuts import render, redirect
from games import forms
from .models import Game, Player
from django.http import HttpResponse
from django.db.models import Count

# Create your views here.

def create_game(request):
    game = forms.GameForm(request.POST or None)
    games = Game.objects.all()
    if game.is_valid():
        game.save()
        return redirect('/games/')
    if games > 0:
        winner_ids = Game.objects.all() \
            .values('winner') \
            .annotate(total=Count('winner_id')) \
            .order_by('-total')[:10]
        winners = Player.objects.filter(pk__in=[w['winner'] for w in winner_ids])
        winners_dict = { w.pk:w.name for w in winners }
        win_tots = [ {'total': w['total'],'name': winners_dict[int(w['winner'])] } for w in winner_ids ]
    return render(request, 'new_game.html', {'form': game,'games':games, 'wins': win_tots})

def games(request):
    games = Game.objects.all()
    return render(request, 'games.html', {'games': games})
   
def create_player(request):
    player = forms.PlayerForm(request.POST or None)
    players = Player.objects.all()
    if player.is_valid():
        player.save()
        return redirect('/players/')
    games = len(Game.objects.all())
    return render(request, 'new_player.html', {'form': player,'players':players})
    
def players(request):
    players = Player.objects.all()
    return render(request, 'players.html', {'players': players})
    