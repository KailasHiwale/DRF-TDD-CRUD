from django.db import models
from django.core.validators import (
    MaxValueValidator,
    MinValueValidator,
    validate_email,
    RegexValidator,
    MinLengthValidator)


class Institute(models.Model):
    """Model for institute details"""
    GOVERNMENT = 'GO'
    GOVERNMENT_AUTONOMOUS = 'GA'
    PRIVATE = 'PR'
    INSTITUTE_TYPE = (
        (GOVERNMENT, 'Government'),
        (GOVERNMENT_AUTONOMOUS, 'Government Autonomous'),
        (PRIVATE, 'Private'),)
    id = models.AutoField(primary_key=True)
    institute_name = models.CharField(max_length=254)
    address = models.CharField(max_length=500)
    pin_code = models.IntegerField(
        validators=[MinValueValidator(100000), MaxValueValidator(999999)],
        blank=True,
        null=True)
    office_mail = models.EmailField(
        max_length=254,
        unique=True,
        validators=[validate_email],
        blank=True,
        null=True)
    phone_number = models.CharField(
        max_length=14,
        validators=[RegexValidator(r'^\d{1,10}$'), MinLengthValidator(10)],
        blank=True,
        null=True)
    website = models.URLField(max_length=150, blank=True, null=True)
    institute_type = models.CharField(
        max_length=150,
        choices=INSTITUTE_TYPE,
        default=GOVERNMENT,
        blank=True,
        null=True)
    founded_in = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(2020)],
        blank=True,
        null=True)
    affiliated_to = models.CharField(max_length=150, blank=True, null=True)
    approved_by = models.CharField(max_length=254, blank=True, null=True)
    owner = models.ForeignKey(
        'auth.User',
        related_name='owner_id',
        on_delete=models.CASCADE,
        db_column='owner')

    def __str__(self):
        return self.institute_name

    class Meta:
        managed = False
        db_table = 'institute'
