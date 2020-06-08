from django.urls import path
from moviebuddy import views

urlpatterns = [
    path('movies/', views.MovieList.as_view(), name='movie-list'),
    path('movies/<int:pk>', views.MovieDetail.as_view(), name='movie-detail'),
    path('reviews/', views.ReviewList.as_view(), name='review-list'),
    path('reviews/<int:pk>', views.ReviewDetail.as_view(), name='review-detail'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user-detail'),
]