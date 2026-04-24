# DRF
from rest_framework.viewsets import ModelViewSet
from rest_framework.serializers import ValidationError
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from django_filters.rest_framework import DjangoFilterBackend
# Models
from .models import Institution, Patient, Profile, Exam

# Serializers
from .serializers import (
    InstitutionListSerializer,
    InstitutionCreateSerializer,
    InstitutionMinSerializer,
    PatientListSerializer,
    PatientCreateSerializer,
    PatientOptionsSerializer,
    ExamFormSerializer,
    ExamListSerializer,
    ProfileListSerializer,
    ProfileFormSerializer,
    ProfileDetailSerializer
)

from .filters import ExamFilterSet, PatientFilterSet

from .mixins import UrlParamMixin

from rest_framework.permissions import IsAuthenticated

from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import get_user_model

User = get_user_model()

class InstitutionViewSet(ModelViewSet):
    queryset = Institution.objects.all()
    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name', 'trade_name', 'cnpj']
    ordering_fields = ['name', 'created_at']

    def get_serializer_class(self):
        if self.action == 'create':
            return InstitutionCreateSerializer
        if self.action == 'options':
            return InstitutionMinSerializer
        return InstitutionListSerializer
    
    @action(detail=False, methods=['get'])
    def options(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.select_related('user', 'institution')
    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['user__email', 'user__username']

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return ProfileFormSerializer
        if self.action == 'retrieve':
            return ProfileDetailSerializer
        return ProfileListSerializer
    
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
class PatientViewSet(ModelViewSet):    
    permission_classes = [IsAuthenticated]
    queryset = Patient.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = PatientFilterSet
    search_fields = ['full_name', 'cpf', 'phone']
    ordering_fields = ['full_name', 'created_at']

    def get_serializer_class(self):
        if self.action == 'create':
            return PatientCreateSerializer
        if self.action == 'options':
            return PatientOptionsSerializer
        return PatientListSerializer
    
    @action(detail=False, methods=['GET'], url_path='options')
    def options(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ExamViewSet(ModelViewSet):
    filterset_class = ExamFilterSet
    parser_classes = [MultiPartParser, FormParser]
    queryset = Exam.objects.all().select_related(
        "patient",
        "profile",
        "institution",
        "profile__user",
    )
    search_fields = ['id', 'patient__full_name', 'profile__full_name']
    filter_backends = [DjangoFilterBackend, SearchFilter]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return ExamListSerializer
        return ExamFormSerializer
    