from django.forms import ModelForm, CharField, TextInput, \
    ModelMultipleChoiceField, SelectMultiple, ModelChoiceField, Select
from .models import Tag, Quote, Author


class TagForm(ModelForm):
    name = CharField(min_length=3, max_length=25,
                     required=True, widget=TextInput())

    class Meta:
        model = Tag
        fields = ['name']


class QuoteForm(ModelForm):
    quote = CharField(min_length=10, max_length=250, required=True, widget=TextInput())
    author = ModelChoiceField(queryset=Author.objects.all().order_by('fullname'), required=True, widget=Select())
    tags = ModelMultipleChoiceField(queryset=Tag.objects.all().order_by("name"), required=True, widget=SelectMultiple())

    class Meta:
        model = Quote
        fields = ['quote', 'author', 'tags']


class AuthorForm(ModelForm):
    fullname = CharField(max_length=50, widget=TextInput())
    born_date = CharField(max_length=50, widget=TextInput())
    born_location = CharField(max_length=150, widget=TextInput())
    description = CharField(widget=TextInput())

    class Meta:
        model = Author
        fields = ["fullname", "born_date", "born_location", "description"]
