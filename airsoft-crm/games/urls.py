from django.urls import path

from . import views

app_name = 'games'
urlpatterns = [
    path('', views.index, name='index'),  # 50
    path('<int:game_id>/', views.game, name='game'),  # 70
    path('<int:game_id>/register_confirm/', views.confirm_registration,
         name='confirm_registration'),  # 50
    path('<int:game_id>/register/', views.game_registration,
         name='game_registration'),  # 50
    ]
