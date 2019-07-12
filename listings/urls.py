from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='listings'),
    path('search', views.search, name='search'),
    path('<int:listing_id>', views.listing, name='listing')
]
