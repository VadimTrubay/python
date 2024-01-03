from django.shortcuts import render, redirect, get_object_or_404
from .forms import TagForm, QuoteForm, AuthorForm
from .models import Tag, Author, Quote
from django.core.paginator import Paginator
# Create your views here.


def main(request):
    quotes_ = Quote.objects.all()
    paginator = Paginator(quotes_, 7)
    page = request.GET.get('page')
    quotes = paginator.get_page(page)
    return render(request, 'quoteapp/index.html', {"quotes": quotes})


def author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quoteapp:main')
        else:
            return render(request, 'quoteapp/author.html', {'form': form})

    return render(request, 'quoteapp/author.html', {'form': AuthorForm()})


def tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quoteapp:main')
        else:
            return render(request, 'quoteapp/tag.html', {'form': form})

    return render(request, 'quoteapp/tag.html', {'form': TagForm()})


def quote(request):
    tags = Tag.objects.all()
    authors = Author.objects.all()
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_quote = form.save()

            choice_authors = Author.objects.filter(name__in=request.POST.getlist('authors'))
            for author in choice_authors.iterator():
                new_quote.authors.add(author)            #
            choice_tags = Tag.objects.filter(tag__in=request.POST.getlist('tags'))
            for tag in choice_tags.iterator():
                new_quote.tags.add(tag)

            return redirect(to='quoteapp:main')
        else:
            return render(request, 'quoteapp/quote.html', {"tags": tags, "authors": authors, 'form': form})

    return render(request, 'quoteapp/quote.html', {"tags": tags, "authors": authors, 'form': QuoteForm()})


def detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'quoteapp/detail.html', {"author": author})


def tag_search(request, _id):
    tags = Tag.objects.filter(id=_id).first()
    quotes_ = Quote.objects.filter(tags=_id).all()
    paginator = Paginator(quotes_, 7)
    page = request.GET.get('page')
    quotes = paginator.get_page(page)

    return render(request, 'quoteapp/tag_search.html', {'quotes': quotes, 'tags': tags})




