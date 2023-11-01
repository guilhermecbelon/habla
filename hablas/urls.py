from django.urls import path

from . import views

app_name = 'hablas'
urlpatterns = [
    path('', views.list_hablas, name='index'),
    path('search/', views.search_hablas, name='search'),
    path('create/', views.create_habla, name='create'),
    path('<int:habla_id>/', views.detail_habla, name='detail'),
]
