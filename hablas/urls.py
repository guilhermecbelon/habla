from django.urls import path

from . import views

app_name = 'hablas'
urlpatterns = [
    path('', views.list_hablas, name='index'),
    path('search/', views.search_hablas, name='search'),
    path('create/', views.create_habla, name='create'),
    path('<int:habla_id>/', views.detail_habla, name='detail'),
    path('<int:habla_id>/delete/', views.delete_habla, name='delete'),
    path('<int:habla_id>/edit/', views.edit_habla, name='edit'),
    path('<int:habla_id>/create_comment/', views.create_comment, name ='create_comment')
]
