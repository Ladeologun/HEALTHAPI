from django.urls import path
from . import views
from menstrual_cycle.views import CreateCycleView

urlpatterns = [
    path('register/', views.RegisterUserView.as_view(),name='register'),
    path('login/', views.LoginView.as_view(),name='login'),
    path('create-cycles/', CreateCycleView.as_view(),name='create-cycle')
]