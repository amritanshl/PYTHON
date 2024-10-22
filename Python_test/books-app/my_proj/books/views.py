from django.shortcuts import render
from .models import Book
from django.views.generic import ListView, CreateView, DeleteView,UpdateView,DetailView
# Create your views here.

class BookList(ListView):
    model = Book

class BookView(DetailView):
    model = Book

class BookCreate(CreateView):
    model = Book
    fields=['name', 'pages']

class BookUpdate(UpdateView):
    model = Book
    fields=['name', 'pages']

class BookDelete(DeleteView):
    model = Book
