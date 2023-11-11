from django.urls import path

from .views import *

app_name = 'hablas'
urlpatterns = [
    path('', ListHablasView.as_view(), name='index'),
     path('create/', CreateHablaView.as_view(), name='create'),
    path('search/', search_hablas, name='search'),
    path('<str:habla_cattegory>/search_by_tag/', search_hablas_by_tag, name='search_by_tag'),
    path('<int:pk>/', DetailHablaView.as_view(), name='detail'),
    path('<int:habla_id>/delete/', delete_habla, name='delete'),
    path('<int:habla_id>/edit/', edit_habla, name='edit'),
    path('<int:habla_id>/like/', like_habla, name='like'),
    path('<int:habla_id>/create_comment/', create_comment, name ='create_comment')
]
