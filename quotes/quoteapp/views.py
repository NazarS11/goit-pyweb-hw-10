from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import AuthorForm, TagForm, QuoteForm
from django.http import JsonResponse
from django.contrib import messages
from .models import Author, Quote, Tag


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
def add_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            tag = form.save()
            messages.success(request, f'Tag "{tag.name}" was successfully added!')
            return redirect(to='quoteapp:add_tag')
        else:
            return render(request, 'quoteapp/tag.html', {'form': form})

    return render(request, 'quoteapp/tag.html', {'form': TagForm()})


def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote = form.save(commit=False)
            quote.user = request.user
            quote.save()
            form.save_m2m() 
            return redirect('quoteapp:main')
    else:
        form = QuoteForm()

    return render(request, 'quoteapp/quote.html', {'form': form})


def my_qoutes(request):
    user = request.user
    quotes = Quote.objects.filter(user=user)
    return render(request, 'quoteapp/my_quotes.html', {"quotes": quotes})


def detail(request, quote_id):
    quote = get_object_or_404(Quote, pk=quote_id)
    author = quote.author  
    return render(request, 'quoteapp/detail.html', {"quote": quote, "author": author})


def author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'quoteapp/author.html', {"author": author})

@login_required
def delete_quote(request, quote_id):
    Quote.objects.get(pk=quote_id, user=request.user).delete()
    return redirect(to='quoteapp:my_quotes')

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
    return render(request, 'quoteapp/edit_quote.html', {'form': form})
