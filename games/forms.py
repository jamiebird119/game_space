from django import forms
from .models import Game, Console, Genre


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('sku',
                  'name',
                  'description',
                  'price',
                  'genres',
                  'consoles',
                  'rating',
                  'release_year',
                  'publisher',
                  'image_url',
                  'image',
                  'special_offer',
                  'offer_percentage',
                  'original_price',
                  'twitch_id',
                  )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'sku': 'Sku',
            'name': 'Name',
            'description': 'Description',
            'price': 'Price',
            'genres': 'Genres',
            'consoles': 'Consoles',
            'rating': 'Rating',
            'release_year': 'Release Year',
            'publisher': 'Publisher',
            'image_url': 'Image Url',
            'image': 'Image',
            'special_offer': 'Special Offer',
            'offer_percentage': 'Offer Percentage',
            'original_price': 'Original Price',
            'twitch_id': 'Twitch Id'
        }
        labels = {
            'genres': 'Genres <small class="text-info"> Hold Ctrl to select multiple values</small>',
            'consoles': 'Consoles  <small class="text-info"> Hold Ctrl to select multiple values</small>',
            'image': 'Image',
            'special_offer': 'Special Offer',
        }
        for field in self.fields:
            if field in labels:
                self.fields[field].label = labels[field]
            else:
                self.fields[field].label = False
            if field != "consoles" and field != "genres" and field != "image":
                self.fields[field].widget.attrs['class'] = 'form-control input'
            elif field == "image":
                self.fields[field].widget.attrs['class'] = 'form-control-file'
            else:
                self.fields[field].widget.attrs['class'] = 'form-control custom-select'
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
        consoles = Console.objects.all()
        genres = Genre.objects.all()
        friendly_names_consoles = [
            (c.id, c.get_friendly_name()) for c in consoles]
        friendly_names_genres = [
            (c.id, c.get_friendly_name()) for c in genres]
        self.fields["consoles"].choices = friendly_names_consoles
        self.fields["genres"].choices = friendly_names_genres
