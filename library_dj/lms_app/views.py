from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import FormBook, FormCat

# Create your views here.
def index(request):
  if request.method == 'POST':
    add_book = FormBook(request.POST, request.FILES)
    if add_book.is_valid():
      add_book.save()

    add_cat = FormCat(request.POST)
    if add_cat.is_valid():
      add_cat.save()

  context = {
    'categorys': Category.objects.all(),
    'books': Book.objects.all(),
    'form': FormBook(),
    'formcat': FormCat(),
    'allbooks': Book.objects.filter(active=True).count(),
    'soldbooks': Book.objects.filter(status='sold').count(),
    'renatlbooks': Book.objects.filter(status='renatl').count(),
    'availbebooks': Book.objects.filter(status='availbe').count(),
  }
  return render(request, 'pages/index.html', context)

def books(request):
  query = Book.objects.all()
  if 'search_name' in request.GET :
    title = request.GET['search_name']
    if title:
      query = query.filter(title__icontains=title)
  context = {
    'categorys': Category.objects.all(),
    'books': query,
    'formcat': FormCat(),
  }
  return render(request, 'pages/books.html', context)

def update(request, id):
  book_id = Book.objects.get(id=id)
  if request.method == 'POST':
    book_save = FormBook(request.POST, request.FILES, instance=book_id)
    if book_save.is_valid():
      book_save.save()
      return redirect('/')
  else:
    book_save = FormBook(instance=book_id)
  context = {
    'form': book_save
  }
  return render(request, 'pages/update.html', context)

def delete(request, id):
  book_del = get_object_or_404(Book, id=id)
  if request.method == 'POST':
    book_del.delete()
    return redirect('/')
  return render(request, 'pages/delete.html')
