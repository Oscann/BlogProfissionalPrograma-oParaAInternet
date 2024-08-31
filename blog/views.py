from django.shortcuts import render
from .models import Project, Technology, Skill, Courses

# Create your views here.
def index(request):
    projects = Project.objects.all()
    technologies = Technology.objects.all()

    context = {
        'projects': projects,
        'technologies': technologies
    }

    return render(request, 'index.html', context)

def about(request):
    skills = Skill.objects.all()
    courses = Courses.objects.all()

    context = {
        "skills": skills,
        "courses": courses
    }

    return render(request, 'about.html', context)