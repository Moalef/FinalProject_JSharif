from django.urls import path
from . import views

app_name = 'ads'

urlpatterns = [
    path('ads/', views.AdListView.as_view(), name='ad_list'),
    path('ad/<pk>/', views.AdDetailView.as_view(), name='ad_detail'),
    path('ads/inbox/', views.AdInboxView.as_view(), name='ad_inbox'),
    path('ads/inbox/<pk>/', views.AdInboxDetailView.as_view(), name='ad_inbox_detail'),
    path('bookmarks/', views.BookmarkListView.as_view(), name='bookmark_list'),
    path('bookmarks/create/', views.BookmarkCreateView.as_view(), name='bookmark_create'),

]
