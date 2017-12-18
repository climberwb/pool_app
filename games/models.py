from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django import forms

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=15,blank=False, null=False, unique=True)
    created_at = models.DateTimeField(default=timezone.now, blank=False)
    
    def __str__(self):
        return self.name
    

class Game(models.Model):
    winner = models.ForeignKey(Player, blank=False, related_name='user_winner', null=False)
    loser = models.ForeignKey(Player, blank=False, related_name='user_loser', null=False)
    created_at = models.DateTimeField(default=timezone.now, blank=False)
    def save(self, *args, **kwargs):
        if self.winner == self.loser:
            raise forms.ValidationError('attempted to create a game object where loser == winner')
        super(Game, self).save(*args, **kwargs)

    