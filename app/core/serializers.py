from django.contrib.auth.models import User

from .models import Institution
from .models import Profile
from .models import Patient
from .models import Exam
from rest_framework import serializers

class InstitutionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = [
            'id',
            'name',
            'trade_name',
            'cnpj',
            'institution_type',
            'city',
            'state',
            'is_active',
        ]
        
class InstitutionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = '__all__'


class InstitutionMinSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Institution
        fields = ['id', 'name']

class PatientListSerializer(serializers.ModelSerializer):
    institution_name = serializers.CharField(source='institution.name', read_only=True)

    class Meta:
        model = Patient
        fields = [
            'id',
            'full_name',
            'cpf',
            'birth_date',
            'gender',
            'phone',
            'institution_name',
            'is_active',
        ]
        
class PatientOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'full_name']
        
class PatientCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
        

class ProfileListSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = Profile
        fields = [
            'id',
            'user',
            'user_email',
            'phone',
            'crm',
            'profile_image',
        ]

class ProfileOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'id',
            'full_name',
        ]
        
class ProfileFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email']
        
class ProfileDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Profile
        fields = '__all__'
        

class ExamListSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    profile = ProfileOptionsSerializer()
    institution = InstitutionMinSerializer()
    patient = PatientOptionsSerializer()
    
    class Meta:
        model = Exam
        fields = [
            "id",
            "institution",
            "profile",
            "patient",
            'image',
            "classification",
            "confidence",
            "created_at",
        ]
        
    def get_image(self, obj):
        request = self.context.get("request")
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None

class ExamFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = [
            "institution",
            "profile",
            "patient",
            "image",
            "description"
        ]