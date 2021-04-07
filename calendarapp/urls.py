from django.urls import path
from . import views
app_name = 'calendarapp'
urlpatterns = [
    path('index', views.index, name='index'),
    path('calendar/', views.CalendarView.as_view(), name='calendar'),
    path('member/', views.MemberView.as_view(), name='member'),
    path('event/new/', views.create_event, name='event_new'),
    path('event/edit/<int:pk>/', views.EventEdit.as_view(), name='event_edit'),
    path('event/<int:event_id>/details/', views.event_details, name='event-detail'),
    path('meeting/<int:event_id>/meeting/', views.meeting_details, name='meeting-detail'),
    path('availability<int:availability_id>/availability/', views.IndicateAvailability, name='Indicate_Availability'),
    path('add_eventmember/<int:event_id>', views.add_eventmember, name='add_eventmember'),
    path('event/<int:pk>/remove', views.EventMemberDeleteView.as_view(), name="remove_event"),
]