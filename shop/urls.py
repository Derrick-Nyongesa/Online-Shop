from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='homePage'),
    path('profile/<username>/', views.profile, name='profile'),
    path('profile/<username>/update', views.edit_profile, name='update'),
    path('category/<category>/', views.category, name='category'),
    path('product/<id>', views.product, name='product'),
    path('search/', views.search, name='search'),
    path('cart', views.cart,name='cart'),
    path('add_cart/<id>/', views.add, name='add_cart'),
    path('remove_cart/<id>/', views.remove, name='remove'),
    path('payment', views.payment,name='payment'),
    path('success', views.success,name='success'),
]
