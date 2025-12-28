from django.urls import path, include
from .views import movie_list, movie_detail


urlpatterns = (
    path("movie/", movie_list, name="movie_list"),
    path("movie/<int:pk>/", movie_detail, name="movie_detail"),
)
