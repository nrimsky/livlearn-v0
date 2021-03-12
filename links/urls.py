from django.urls import path

from . import views

app_name = 'links'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.LinkDetailView.as_view(), name='detail'),
    path('like/<int:pk>', views.like, name="like"),
    path('search', views.SearchResultsView.as_view(), name='search_results')
]