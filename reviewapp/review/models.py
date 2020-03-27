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

    def __str__(self):
        return self.institute_name

    class Meta:
        managed = False
        db_table = 'institute'


class Reviewer(models.Model):
    STUDENT = 'ST'
    WORKING = 'WR'
    PROFESSION_STATUS = (
        (STUDENT, 'Student'),
        (WORKING, 'Working'),
    )
    user_id = models.IntegerField()
    reviewer_name = models.CharField(max_length=150)
    email_id = models.EmailField(
        max_length=254,
        unique=True,
        validators=[validate_email]
    )
    profession_status = models.CharField(
        max_length=150,
        choices=PROFESSION_STATUS,
        default=STUDENT,
        blank=True,
        null=True
    )
    city = models.CharField(max_length=150, blank=True, null=True)
    state = models.CharField(max_length=150, blank=True, null=True)
    country = models.CharField(max_length=150, default='India', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reviewer'


class Review(models.Model):
    id = models.AutoField(primary_key=True)
    institute = models.ForeignKey('Institute', on_delete=models.CASCADE)
    reviewer = models.ForeignKey('Reviewer', on_delete=models.CASCADE)
    overall_rating = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        blank=True,
        null=True)
    review_title = models.CharField(max_length=254, blank=True, null=True)
    merits = models.CharField(max_length=500, blank=True, null=True)
    demerits = models.CharField(max_length=500, blank=True, null=True)
    advice = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'review'
