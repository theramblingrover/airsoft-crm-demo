from django.urls import path

from . import views

app_name = "players"
urlpatterns = [
    path("", views.index, name="index"),  # 50
    path('new/', views.add_player, name='add_player'),  # 100
    path('<int:player_id>/', views.player, name='player'),  # 50
    path('<int:player_id>/add_purchase/', views.add_purchase,  # 70
         name='add_purchase'),
    path('<int:player_id>/edit/', views.player_edit,  # 100
         name='edit_player'),
    path('<int:player_id>/qr/', views.get_qr, name='get_qr'),  # 120
    path('<int:player_id>/add_achive/', views.add_achive,  # 70
         name='add_achive'),
    ]
