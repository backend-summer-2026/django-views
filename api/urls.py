from django.urls import path

from .views import items_view, ItemsView


urlpatterns = [
    path('items-fbv/', items_view, name='item-url'),
    path('items-cbv/', ItemsView.as_view(), name='item-url'),
]
