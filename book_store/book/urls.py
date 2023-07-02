from django.urls import path
from book.views import home,store_book,show_book

urlpatterns = [
    path('', home, name='homepage'),
    path('store_new_book/', store_book, name='storebook'),
    path('show_book/', show_book, name='showbook'),
]