from django.forms import ModelForm, CharField, TextInput
from .models import Tag, Quote, Author


class AuthorForm(ModelForm):
    name = CharField(min_length=3, max_length=50, required=True, widget=TextInput())
    born_date = CharField(min_length=3, max_length=50, required=True, widget=TextInput())
    born_location = CharField(min_length=3, max_length=500, required=True, widget=TextInput())
    description = CharField(min_length=3, max_length=5000, required=True, widget=TextInput())

    class Meta:
        model = Author
        fields = ['name', 'born_date', 'born_location', 'description']


class TagForm(ModelForm):
    tag = CharField(min_length=3, max_length=50, required=True, widget=TextInput())

    class Meta:
        model = Tag
        fields = ['tag']


class QuoteForm(ModelForm):
    quote = CharField(min_length=10, max_length=5000, required=True, widget=TextInput())

    class Meta:
        model = Quote
        fields = ['quote']
        exclude = ['authors', 'tags']





