from django.urls import path
from . import views

app_name = 'planner'
urlpatterns = [
    path('', views.index, name='index' ),
    path('calendar', views.CalendarView.as_view(), name='calendar'), # here
]