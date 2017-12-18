from django.shortcuts import render, redirect
from games import forms
from django.http import HttpResponse
from django.db.models import Count
from games.models import Player,Game

def home(request):
    win_tots=None
    games = Game.objects.count()
    if games > 0:
        winner_ids = Game.objects.all() \
            .values('winner') \
            .annotate(total=Count('winner_id')) \
            .order_by('-total')[:10]
        winners = Player.objects.filter(pk__in=[w['winner'] for w in winner_ids])
        winners_dict = { w.pk:w.name for w in winners }
        win_tots = [ {'total': w['total'],'name': winners_dict[int(w['winner'])] } for w in winner_ids ]
    return render(request, 'index.html', { 'wins': win_tots})