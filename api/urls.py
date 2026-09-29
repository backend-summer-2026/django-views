from django.urls import path

from .views import ItemsView, items_view


urlpatterns = [
    path('items-fbv/', items_view, name='item-url'),
    path('items-cbv/', ItemsView.as_view(), name='item-url'),
]
