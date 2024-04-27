from django.urls import path
from . import views

app_name = 'ads'

urlpatterns = [
    path('ads/', views.AdListView.as_view(), name='ad_list'),
    path('ad/<pk>/', views.AdDetailView.as_view(), name='ad_detail'),

]
