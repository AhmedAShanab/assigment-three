from django.db import models


class Student(models.Model):
    """
    Student model containing personal and academic information.
    
    Field Choices Documentation:
    - full_name: CharField (max 200) - Text field for storing names, suitable for variable length text
    - university_id: CharField (max 20, unique) - String to preserve leading zeros and special formats
    - age: PositiveIntegerField - Age cannot be negative, integer type is appropriate
    - date_of_birth: DateField - Dedicated date type for calendar dates with validation
    - address: TextField - Long text field for potentially multi-line addresses
    - salary: DecimalField (10 digits, 2 decimal places) - Precise decimal for monetary values
    - photo: ImageField - Django's specialized field for handling image uploads
    """
    
    full_name = models.CharField(
        max_length=200, 
        verbose_name="Full Name",
        help_text="Enter the student's full name"
    )
    
    university_id = models.CharField(
        max_length=20, 
        unique=True,
        verbose_name="University ID Number",
        help_text="Unique university identification number"
    )
    
    age = models.PositiveIntegerField(
        verbose_name="Age",
        help_text="Age in years"
    )
    
    date_of_birth = models.DateField(
        verbose_name="Date of Birth",
        help_text="Birth date in YYYY-MM-DD format"
    )
    
    address = models.TextField(
        verbose_name="Address",
        help_text="Full residential address"
    )
    
    salary = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        verbose_name="Salary",
        help_text="Monthly salary amount"
    )
    
    photo = models.ImageField(
        upload_to='photos/',
        verbose_name="Photo",
        help_text="Profile photo"
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.full_name} ({self.university_id})"
