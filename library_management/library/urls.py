from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='admin_login/')),  # Add this line
    #admin urls
    path('admin_signup/', views.admin_signup, name='admin_signup'),
    path('admin_login/', views.admin_login, name='admin_login'),

    #book management urls
    path('dashboard/', views.view_books, name='dashboard'),
    path('add_book/', views.add_book, name='add_book'),
    path('update_book/<int:book_id>/', views.update_book, name='update_book'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
    
    #student view urls
    path('view_books/', views.view_books, name='view_books'),
]