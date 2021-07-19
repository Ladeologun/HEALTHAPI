from django.urls import path
from menstrual_cycle.views import CreateCycleView
from menstrual_cycle.get_view import ListCycleEvent

urlpatterns = [
    path('cycle-event/', ListCycleEvent.as_view(),name='list-cycle')
]