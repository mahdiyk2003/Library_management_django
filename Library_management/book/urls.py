from django.urls import path
from . import views


app_name = 'book'
urlpatterns = [
    path('', views.home, name='home'),
    path('<id>/', views.single, name='singleBook'),
    path('borrow/<id>/', views.borrow, name='borrow'),
    path('search/', views.search, name='search'),
    path('categories/<name>', views.categories, name='categories'),

]
