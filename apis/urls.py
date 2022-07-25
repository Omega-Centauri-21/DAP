from django.urls import path, include
import apis.views as api_view
from django.contrib import admin


urlpatterns = [
    path('patients/', api_view.DetailView.as_view()),
    path('hospitals/', api_view.AttendanceView.as_view()),
    path('medical_history/', api_view.MarksView.as_view()),
    path('current_status/', api_view.TimetableView.as_view()),
]
