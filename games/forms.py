from django import forms
from .models import Game, Console, Genre


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            consoles = Console.objects.all()
            genres = Genre.objects.all()
            friendly_names_consoles = [(c.id, c.get_friendly_name()) for c in consoles]
            friendly_names_genres = [(c.id, c.get_friendly_name()) for c in genres]

            self.fields["console"].choices = friendly_names_consoles
            self.fields["genres"].choices = friendly_names_genres
            for field_name, field in self.fields.items():
                field.widget.attr['class'] = "form-control"
