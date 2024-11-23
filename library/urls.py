from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('books/', views.books_list, name='books_list'),
    path('books/create/', views.books_create, name='books_create'),
    path('books/<int:pk>/edit/', views.books_edit, name='books_edit'),
    path('books/<int:pk>/delete/', views.books_delete, name='books_delete'),

    path('categories/', views.categories_list, name='categories_list'),
    path('categories/create/', views.categories_create, name='categories_create'),
    path('categories/<int:pk>/edit/', views.categories_edit, name='categories_edit'),
    path('categories/<int:pk>/delete/', views.categories_delete, name='categories_delete'),

    path('members/create/', views.members_create, name='members_create'),
    path('members/<int:pk>/edit/', views.members_edit, name='members_edit'),
    path('members/<int:pk>/delete/', views.members_delete, name='members_delete'),
    path('members/', views.members_list, name='members_list'),

    path('borrows/', views.borrows_list, name='borrows_list'),
    path('borrows/create/', views.borrows_create, name='borrows_create'),
    path('borrows/<int:pk>/edit/', views.borrows_edit, name='borrows_edit'),
    path('borrows/<int:pk>/delete/', views.borrows_delete, name='borrows_delete'),
]