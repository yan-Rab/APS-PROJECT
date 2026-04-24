from django.contrib import admin
from django.urls import path
from core.views import login_view
from core.views import get_csrf_token
from core.views import check_auth
from core.views import logout_view
from django.conf.urls.static import static
from django.urls import include
from django.conf import settings

from rest_framework.routers import DefaultRouter
from django.urls import path

from .api import (
    InstitutionViewSet,
    PatientViewSet,
    ProfileViewSet,
    ExamViewSet
)

router = DefaultRouter()
router.register(r'institutions', InstitutionViewSet, basename='institution')
router.register(r'patients', PatientViewSet, basename='patient')
router.register(r'profiles', ProfileViewSet, basename='profile')
router.register(r'exams', ExamViewSet, basename='exam')

urlpatterns = [
    path('login/', login_view, name='login'),
    path("csrf/", get_csrf_token),
    path("me/", check_auth, name="check_auth"),
    path("logout/", logout_view, name="logout"),
    path("api-auth/", include("rest_framework.urls")),
    path('', include(router.urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


