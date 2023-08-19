from django.shortcuts import render
from .models import Project, Skill, Blog, Education, Experience

# Create your views here.

def index(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    blogs = Blog.objects.all()
    educations = Education.objects.all()
    experiences = Experience.objects.all()
    context = {'projects':projects, 'skills':skills, 'blogs':blogs, 'educations':educations, 'experiences':experiences}
    return render(request,'portfolio/index.html', context)

def details(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    blogs = Blog.objects.all()
    context = {'blog':blog, 'blogs':blogs}
    return render(request,'portfolio/details.html', context)
