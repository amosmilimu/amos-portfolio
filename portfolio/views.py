from django.shortcuts import render
from .models import Project, Skill, Blog

# Create your views here.

def index(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    blogs = Blog.objects.all()
    context = {'projects':projects, 'skills':skills, 'blogs':blogs}
    return render(request,'portfolio/index.html', context)
