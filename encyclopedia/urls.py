from django.urls import path
from . import views

app_name = 'encyclopedia'

urlpatterns = [
    path("", views.index, name="index"),
    path('<str:title>', views.entry_page, name='entry_page'),
    path('search/', views.search, name='search'),
    path('new/', views.create_new_page, name='create_new_page'),
    path('edit/', views.edit_page, name='edit'),
    path('random/', views.random_page, name='random_page')
]
