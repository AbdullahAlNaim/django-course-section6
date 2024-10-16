from django.shortcuts import get_object_or_404, render
from django.http import Http404
from .models import Book
from django.db.models import Avg, Sum, Min, Max, Count

# Create your views here.

def index(request):
    allBooks = Book.objects.all().order_by('title')
    totalBooks = allBooks.count()
    avgRating = allBooks.aggregate(Avg('rating'))

    return render(request, 'book_outlet/index.html', {
        'books': allBooks,
        'total_number_of_books': totalBooks,
        'average_rating': avgRating
    })

def book_detail(request, slug):
    # try:
    #     book = Book.objects.get(pk=id)
    # except:
    #     raise Http404()
    # this is a quicker version of whats shwon above
    book = get_object_or_404(Book, slug=slug)

    return render(request, 'book_outlet/book_detail.html', {
        'title': book.title,
        'author': book.author,
        'rating': book.rating,
        'is_bestseller': book.is_bestselling
    })