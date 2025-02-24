from django.shortcuts import (
    render,
    # get_object_or_404
)
from django.http import Http404
from django.db.models import Avg

from .models import Book

# Create your views here.


def index(request):
    books = Book.objects.all().order_by('title')
    # aggregation methods
    num_books = books.count()
    avg_rating = books.aggregate(Avg("rating"))

    context = {
        "books": books,
        "total_books_num": num_books,
        "avg_rating": avg_rating,
    }
    return render(request, 'book_outlet/index.html', context)


def book_detail(request, slug):
    # book = get_object_or_404(Book, pk=pk)
    try:
        # book = Book.objects.get(id=pk)  # or .get(pk=variable)
        book = Book.objects.get(slug=slug)
    except Exception:
        raise Http404()

    context = {
        "book": book
    }
    return render(request, 'book_outlet/book.html', context)
