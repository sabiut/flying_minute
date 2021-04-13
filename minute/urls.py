from django.urls import path
from . import views
from .views import signup, user_logout

urlpatterns = [
    path('', views.index, name="index"),
    path('login_page/', views.login_page, name='login_page'),
    path('log_out/', views.log_out, name ='log_out'),
    path('minute/', views.minute_form, name='minute'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_board_members/', views.add_board_members, name='add_board_members'),
    path('display_board_members/', views.display_board_members, name='display_board_members'),
    path('signup/', signup, name='signup'),
    path('logout/', user_logout, name='logout'),
    path('upload_file/', views.upload_file, name='upload_file'),
    path(r'<int:member_id>/update_member/', views.update_member_form, name='update_member'),
    path(r'<int:minutes_id>/update_flyminute/', views.update_fly_minute_form, name='update_fly_minute'),
    path(r'<int:member_id>/delete_member/', views.drop_member, name='drop_member'),
    path(r'minutes/', views.minutes, name='minutes'),
    path('add_member_present_form/', views.add_member_present_form, name='add_member_present_form'),
    path('DisplayGenetratedMinutes/', views.DisplayGenetratedMinutes, name='DisplayGenetratedMinutes'),
    path(r'<int:flyminute_id>/bord_minute', views.MinutesReport, name='MinutesReport'),
    path(r'<int:report_id>/report', views.display_report, name='display_report'),
    path('commentForm/', views.commentForm, name='commentForm'),
    path(r'<int:auth_minutes_id>/authorize_minute', views.authorize_minute_form, name='authorize_minute'),

]
