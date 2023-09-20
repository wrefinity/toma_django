
from django.urls import path
from .views import HomePageView, LoginView, SignupView, LogoutView

urlpatterns = [
    path('dashboard', HomePageView.as_view(), name="home"),
    path("register", SignupView.as_view(), name="register"),
    path("", LoginView.as_view(), name="login"),
    path("logout", LogoutView.as_view(), name="logout")
]