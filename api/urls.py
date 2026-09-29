from django.urls import path

from .views import items_view, ItemsView, UserCreateView


urlpatterns = [
    path('items-fbv/', items_view, name='item-fbv-url'),
    path('items-cbv/', ItemsView.as_view(), name='item-cbv-url'),
    path('users/', UserCreateView.as_view(), name='user-create')
]
