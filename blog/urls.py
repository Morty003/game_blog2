from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

urlpatterns = [
    path('reviews/', views.ReviewView.as_view(), name='reviews'),
    path('search/', views.Search.as_view(), name='search'),
    path('comment/<int:pk>', views.CreateComment.as_view(), name='comment'),
    path('category/<slug:category_slug>/', views.PostListView.as_view(), name='post_list'),
    path('post/<slug:category_slug>/<slug:post_slug>/', views.PostDetailView.as_view(), name='post_single'),
    path('', views.HomeView.as_view(), name='home'),
]