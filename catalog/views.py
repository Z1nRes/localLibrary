from django.shortcuts import render

# Create your views here.
from .models import Book, Author, BookInstance, Genre


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()

    num_genres = Genre.objects.count()
    num_filtered_books = Book.objects.all().filter(title__iregex="ПрОгрАммиРованИе").count()

    return render(
        request,
        'index.html',
        context=
        {'num_books': num_books, 'num_instances': num_instances, 'num_instances_available': num_instances_available,
         'num_authors': num_authors, 'num_genres': num_genres, 'num_filtered_books': num_filtered_books},
    )
