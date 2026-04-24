from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from .constants import INSTITUTION_TYPE_CHOICES
from .constants import GENDER_CHOICES


def validate_file_size(file):
    max_size = 2 * 1024 * 1024  # 2MB

    if file.size > max_size:
        raise ValidationError("O arquivo deve ter no máximo 2MB.")


class Institution(models.Model):
    # Identificação básica
    name = models.CharField(max_length=255)
    trade_name = models.CharField(max_length=255, blank=True)  # nome fantasia
    cnpj = models.CharField(max_length=18, unique=True)

    institution_type = models.CharField(
        max_length=20,
        choices=INSTITUTION_TYPE_CHOICES,
        default='hospital'
    )

    # Contato
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    website = models.URLField(blank=True)

    # Endereço
    street = models.CharField(max_length=255)
    number = models.CharField(max_length=20)
    complement = models.CharField(max_length=255, blank=True)
    neighborhood = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=10)
    country = models.CharField(max_length=100, default='Brazil')

    # Dados operacionais
    is_active = models.BooleanField(default=True)
    capacity = models.IntegerField(null=True, blank=True)  # número de leitos, por exemplo

    # Auditoria
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    full_name = models.CharField(max_length=50, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    specialty = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True, null=True)
    institution = models.ForeignKey(
        'Institution',
        on_delete=models.SET_NULL,
        related_name='profiles',
        null=True
    )
    crm = models.CharField(max_length=20)
    profile_image = models.ImageField(
        upload_to='users/profile_images/',
        validators=[FileExtensionValidator(['jpg', 'jpeg', 'png']), validate_file_size],
        null=True,
        blank=True
    )
    
    def __str__(self):
        return self.user.username
    
    
class Patient(models.Model):
    full_name = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, unique=True)

    birth_date = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20)

    street = models.CharField(max_length=255, blank=True)
    number = models.CharField(max_length=20, blank=True)
    neighborhood = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=2, blank=True)
    zip_code = models.CharField(max_length=10, blank=True)

    institution = models.ForeignKey(
        'Institution',
        on_delete=models.SET_NULL,
        null=True,
        related_name='patients'
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name
    
class Exam(models.Model):
    class ClassificationChoices(models.TextChoices):
        BENIGN = "benign", "Benigno"
        MALIGNANT = "malignant", "Maligno"
        NORMAL = "normal", "Normal"

    institution = models.ForeignKey(
        "core.Institution",
        on_delete=models.CASCADE,
        related_name="exams"
    )

    profile = models.ForeignKey(
        "core.Profile",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="exams"
    )

    patient = models.ForeignKey(
        "core.Patient",
        on_delete=models.CASCADE,
        related_name="exams"
    )

    image = models.ImageField(
        upload_to="exams/",
        null=True,
        blank=True
    )
    
    description = models.TextField(blank=True)
    
    classification = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        choices=ClassificationChoices.choices
    )

    confidence = models.FloatField(null=True, blank=True)  # valor entre 0 e 1 (ou % se preferir)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Exam {self.id} - {self.patient_id} - {self.classification}"