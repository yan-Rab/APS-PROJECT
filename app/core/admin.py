from django.contrib import admin
from .models import Institution, Patient, Profile, Exam

@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'trade_name',
        'cnpj',
        'institution_type',
        'city',
        'state',
        'is_active',
    )

    search_fields = (
        'name',
        'trade_name',
        'cnpj',
    )

    list_filter = (
        'institution_type',
        'state',
        'is_active',
    )

    ordering = ('name',)
    
    
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'full_name',
        'cpf',
        'birth_date',
        'gender',
        'phone',
        'institution',
        'is_active',
    )

    search_fields = (
        'full_name',
        'cpf',
        'phone',
    )

    list_filter = (
        'gender',
        'is_active',
        'institution',
    )

    autocomplete_fields = ('institution',)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related('institution')
    

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'get_email',
        'institution',
        'phone',
    )

    search_fields = (
        'user__username',
        'user__email',
    )

    list_filter = (
        'institution',
    )

    autocomplete_fields = ('user', 'institution')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related('user', 'institution')

    def get_email(self, obj):
        return obj.user.email
    get_email.short_description = 'Email'
    

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('id', 'institution', 'profile', 'patient', 'created_at')
    search_fields = (
        'profile__full_name',
        'patient__full_name',
    )
    list_filter = ('institution', 'created_at')