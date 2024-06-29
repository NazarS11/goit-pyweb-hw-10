from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import AuthorForm, TagForm, QuoteForm
from django.http import JsonResponse
from .models import Author, Quote, Tag


# Create your views here.
def main(request):
    quotes = Quote.objects.all()
    return render(request, 'quoteapp/index.html', {"quotes": quotes})

@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quoteapp:main')
        else:
            return render(request, 'quoteapp/add_author.html', {'form': form})

    return render(request, 'quoteapp/add_author.html', {'form': AuthorForm()})

@login_required
def tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quoteapp:main')
        else:
            return render(request, 'quoteapp/tag.html', {'form': form})

    return render(request, 'quoteapp/tag.html', {'form': TagForm()})

@login_required
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote = form.save(commit=False)
            quote.user = request.user
            tags = request.POST.getlist('tags')
            quote.save()
            for tag_id in tags:
                tag = Tag.objects.get(id=tag_id)
                quote.tags.add(tag)
            return redirect('quoteapp:main')  # Заміна на ваш шлях
    else:
        form = QuoteForm()
        authors = Author.objects.all()
        tags = Tag.objects.all()

    return render(request, 'quoteapp/quote.html', {'form': form, 'authors': authors, 'tags': tags})


def my_qoutes(request):
    user = request.user
    quotes = Quote.objects.filter(user=user)
    return render(request, 'quoteapp/my_quotes.html', {"quotes": quotes})


def detail(request, quote_id):
    quote = get_object_or_404(Quote, pk=quote_id)
    author = quote.author  # Отримуємо автора через об'єкт цитати
    return render(request, 'quoteapp/detail.html', {"quote": quote, "author": author})


def author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'quoteapp/author.html', {"author": author})

@login_required
def delete_quote(request, quote_id):
    Quote.objects.get(pk=quote_id, user=request.user).delete()
    return redirect(to='quoteapp:main')

@login_required
def edit_quote(request, quote_id):
    quote = get_object_or_404(Quote, pk=quote_id)
    if request.method == "POST":
        form = QuoteForm(request.POST, instance=quote)
        if form.is_valid():
            form.save()
            return redirect('quoteapp:main')
    else:
        form = QuoteForm(instance=quote)
    return render(request, 'quoteapp/edit_quote.html', {'form': form, 'quote': quote})

