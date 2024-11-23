from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Category, Member, Borrow
from .forms import BookForm, BorrowForm, CategoryForm, MemberForm
from django.template.loader import get_template
from django.http import HttpResponse

def home(request):
    return render(request, 'library/index.html')

# ======BOOK LIST=====
def books_list(request):
    books = Book.objects.all()
    return render(request, 'library/books_list.html', {'books': books})

# Create 
def books_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books_list')
    else:
        form = BookForm()
    return render(request, 'library/books_form.html', {'form': form})

# Edit 
def books_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'library/books_form.html', {'form': form})


# Delete 
def books_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('books_list')
    return render(request, 'library/books_confirm_delete.html', {'book': book})

# ======CATEGORY LIST=====
def categories_list(request):
    categories = Category.objects.all()
    return render(request, 'library/categories_list.html', {'categories': categories})

def categories_create(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories_list')
    else:
        form = CategoryForm()
    return render(request, 'library/categories_form.html', {'form': form})

def categories_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'library/categories_form.html', {'form': form})

def categories_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('categories_list')
    return render(request, 'library/categories_confirm_delete.html', {'category': category})

# ======MEMBER LIST=====
def members_list(request):
    members = Member.objects.all()
    return render(request, 'library/members_list.html', {'members': members})

def members_create(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('members_list')
    else:
        form = MemberForm()
    return render(request, 'library/members_form.html', {'form': form}) 

def members_edit(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == "POST":
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('members_list')
    else:
        form = MemberForm(instance=member)
    return render(request, 'library/members_form.html', {'form': form})

def members_delete(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        member.delete()
        return redirect('members_list')
    return render(request, 'library/members_confirm_delete.html', {'member': member})


# ======BORROW LIST=====
def borrows_list(request):
    borrows = Borrow.objects.all()
    return render(request, 'library/borrows_list.html', {'borrows': borrows})

def borrows_create(request):
    if request.method == "POST":
        form = BorrowForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('borrows_list')
    else:
        form = BorrowForm()
    return render(request, 'library/borrows_form.html', {'form': form})

def borrows_edit(request, pk):
    borrow = get_object_or_404(Borrow, pk=pk)
    if request.method == "POST":
        form = BorrowForm(request.POST, instance=borrow)
        if form.is_valid():
            form.save()
            return redirect('borrows_list')
    else:
        form = BorrowForm(instance=borrow)
    return render(request, 'library/borrows_form.html', {'form': form})

def borrows_delete(request, pk):
    borrow = get_object_or_404(Borrow, pk=pk)
    if request.method == 'POST':
        borrow.delete()
        return redirect('borrows_list')
    return render(request, 'library/borrows_confirm_delete.html', {'borrow': borrow})
    