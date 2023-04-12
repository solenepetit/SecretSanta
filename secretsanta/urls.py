from django.urls import path
from . import views


urlpatterns = [
    path('', views.santa_group_list, name='santa_group_list'),
    path('santa_group/<int:pk>/', views.santa_group_detail, name='santa_group_detail'),
    path('santa_group/new/', views.santa_group_new, name='santa_group_new'),
    path('santa_group/<int:pk>/edit/', views.santa_group_edit, name='santa_group_edit'),
    # path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # path('post/new/', views.post_new, name='post_new'),
    # path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]
