from django.urls import path
from . import views
urlpatterns = [
    path('',views.fruit_list,name='fruit_list'),
    path('order/',views.place_order,name='place_order'),
]