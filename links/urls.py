from django.urls import path

from . import views

app_name = 'links'

urlpatterns = [
    path('', views.SearchList.as_view(), name='index'),
    path('suggest/', views.suggest, name='suggest'),
    path('<int:pk>/', views.LinkDetailView.as_view(), name='detail'),
    path('post/ajax/like', views.postLike, name='post_like'),
]