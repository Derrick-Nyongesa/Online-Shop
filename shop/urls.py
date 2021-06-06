from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='homePage'),
    path('profile/<username>/', views.profile, name='profile'),
]
