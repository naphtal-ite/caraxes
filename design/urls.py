from django.urls import path
from . import views

urlpatterns = [
    path('author/',views.home,name='author'),
    path('about/',views.about,name='about'),
    path('',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('register/',views.register,name='register'),
    path('add/',views.add_record,name='add'),
    path('book/',views.book,name='book'),
    path('add_book/',views.add_book,name='add_book'),
   # path('update/<int:pk>/',views.update,name='update'),
    path('author/update/<int:pk>/', views.update, name='update'),
    path('book/update_book/<int:pk>/', views.update_book, name='update_book'),
    path('book/delete_book/<int:pk>', views.delete_book, name='delete_book'),
    path('delete_author/<int:pk>', views.delete_author, name='delete_author'),
]
