from django.urls import path

from users.views import LoginView, TokenRefreshView, UserView, UsersView, LogoutView


urlpatterns = [
    path("users/", UsersView.as_view()),
    path("login", LoginView.as_view()),
    path("token/refresh", TokenRefreshView.as_view()),
    path("logout", LogoutView.as_view()),
    path("user/<int:id>/", UserView.as_view()),
]
