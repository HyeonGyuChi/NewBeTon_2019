from django.urls import path
from schedule import views
app_name = 'schedule'

urlpatterns = [
    path('userlist/', views.userlist, name = 'userlist'),
    path('<int:user_id>/detail', views.detail, name = "detail"),
    path('team/<int:team_id>/', views.team, name = "team")
]
