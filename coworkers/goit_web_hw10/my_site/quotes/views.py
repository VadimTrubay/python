from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from bson.objectid import ObjectId


from .forms import TagForm, QuoteForm, AuthorForm
from .models import Tag, Quote, Author
# from .utils import get_mongodb

# Create your views here.
def main(request, page=1):
    # db = get_mongodb()        # for mongodb
    # quotes = db.quote.find()  # for mongodb
    quotes = Quote.objects.all()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.get_page(page)
    
    return render(request, 'quotes/index.html', context={'quotes': quotes_on_page})


def index(request):
    host = request.META["HTTP_HOST"]  # получаем адрес сервера
    user_agent = request.META["HTTP_USER_AGENT"]    # получаем данные бразера
    path = request.path     # получаем запрошенный путь
    user_ip = request.META["REMOTE_ADDR"]

    return HttpResponse(f"""<h2>Hello, world. This is my first site.</h2>
        <p>Host: {host}</p>
        <p>Path: {path}</p>
        <p>User-agent: {user_agent}</p>
        <p>User-ip: {user_ip}
    """)

@login_required
def quote(request):
    tags = Tag.objects.all()
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_quote = form.save()
            choice_tags = Tag.objects.filter(name__in=request.POST.getlist('tags'))
            for tag in choice_tags.iterator():
                new_quote.tags.add(tag)
            return redirect(to='quotes:main')
        else:
            return render(request, 'quotes/quote.html', {"tags": tags, 'form': form})
    return render(request, 'quotes/quote.html', {"tags": tags, 'form': QuoteForm()})
    

@login_required
def tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotes:main')
        else:
            return render(request, 'quotes/tag.html', {'form': form})
    return render(request, 'quotes/tag.html', {'form': TagForm()})


@login_required
def author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotes:main')
        else:
            return render(request, 'quotes/author.html', {'form': form})
    return render(request, 'quotes/author.html', {'form': AuthorForm()})


def author_about(request, pk):
    # db = get_mongodb()
    # author = db.author.find_one({'_id':ObjectId(d)})
    author = Author.objects.get(pk=pk)
    return render(request, 'quotes/author_about.html', context={'author': author})


def tag_search(request, _id):
    tag = Tag.objects.filter(id=_id).first()
    quotes = Quote.objects.filter(tags=_id).all()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    page_number = request.GET.get('page')
    quotes_on_page = paginator.get_page(page_number)
    
    return render(request, 'quotes/tag_search.html', context={'quotes': quotes_on_page, 'tag': tag})