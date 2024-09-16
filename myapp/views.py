from django.shortcuts import render, get_object_or_404
from .models import Book

# Existing book_list view
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

# Add the book_detail view
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)  # Fetch the specific book by primary key (pk)
    return render(request, 'book_detail.html', {'book': book})
