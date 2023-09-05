import pickle

from django.http import HttpResponse
from django.shortcuts import render
from .fuel_parser.fuel_parser.spiders.prices import file


def index(request):

    with open(file, 'rb') as fh:
        data = pickle.load(fh)
        date = data[0]['date'][:10]
    return render(request, 'fuel_list/index.html', {"data": data, "date": date})
