from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),
] 