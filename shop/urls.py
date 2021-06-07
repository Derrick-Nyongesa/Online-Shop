from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='homePage'),
    path('profile/<username>/', views.profile, name='profile'),
    path('profile/<username>/update', views.edit_profile, name='update'),
    path('category/<category>/', views.category, name='category'),
    path('product/<id>', views.product, name='product'),
]
