from django.contrib import admin
from django.urls import path
from core.views import login_view
from core.views import get_csrf_token
from core.views import check_auth
from core.views import logout_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path("csrf/", get_csrf_token),
    path("me/", check_auth, name="check_auth"),
    path("logout/", logout_view, name="logout"),
]
