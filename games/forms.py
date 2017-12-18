from django.forms import ModelForm
from .models import Player, Game



class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = ['name']
        
class GameForm(ModelForm):
    class Meta:
        model = Game
        fields = ['winner','loser']
    def clean(self):
        cleaned_data = super(GameForm,self).clean()
        loser = cleaned_data.get("loser")
        winner = cleaned_data.get("winner")

        if loser == winner:
            msg = "you cannot have loser == winner"
            self.add_error('loser', msg)
            self.add_error('winner', msg)
        