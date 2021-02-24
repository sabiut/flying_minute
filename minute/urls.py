from django.urls import path
from . import views
from .views import signup, user_logout

urlpatterns = [
    path('', views.index, name="index"),
    path('login_page/', views.login_page, name='login_page'),
    path('minute/', views.minute_form, name='minute'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_board_members/', views.add_board_members, name='add_board_members'),
    path('display_board_members/', views.display_board_members, name ='display_board_members'),
    path('signup/', signup, name='signup'),
    path('logout/', user_logout, name='logout'),

]
