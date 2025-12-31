from django.shortcuts import render
from .models import Student


def home_page(request):
    """
    View for the Home Page that displays all students.
    """
    students = Student.objects.all()
    context = {
        'students': students,
        'page_title': 'Home Page - Student Management System'
    }
    return render(request, 'base/home.html', context)
