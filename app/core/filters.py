from django_filters.filterset import FilterSet
from .models import Exam, Patient

class ExamFilterSet(FilterSet):
    class Meta:
        model = Exam
        fields = ['institution', 'profile', 'patient', 'created_at']
        

class PatientFilterSet(FilterSet):
    class Meta:
        model = Patient
        fields = ['institution', 'gender']