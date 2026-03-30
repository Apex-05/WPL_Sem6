from django.shortcuts import render, redirect
from .forms import AuthorForm, PublisherForm, BookForm
from .models import Book

# Create Author
def add_author(request):
    form = AuthorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('add_author')

    return render(request, 'author_form.html', {'form': form})


# Create Publisher
def add_publisher(request):
    form = PublisherForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('add_publisher')

    return render(request, 'publisher_form.html', {'form': form})


# Create Book
def add_book(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('add_book')

    return render(request, 'book_form.html', {'form': form})


# Retrieve Books
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})