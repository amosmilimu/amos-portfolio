from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Project, Skill, Blog, Education, Experience, Contact, CV, GeneralSkill, YearsOfExperience

# Create your views here.

def index(request):
    projects = Project.objects.all().order_by('-priority')
    skills = Skill.objects.all().order_by('-priority')
    blogs = Blog.objects.all().order_by('-priority')
    educations = Education.objects.all().order_by('-priority')
    experiences = Experience.objects.all().order_by('-priority')
    generalSkills = GeneralSkill.objects.all().order_by('-priority')
    if YearsOfExperience.objects.all():
        yearsOfExperience = YearsOfExperience.objects.all()[0]
    else:
        yearsOfExperience = YearsOfExperience( years=5 )

    if CV.objects.all():
        cv = CV.objects.all()[0]
    else:
        cv = None
    context = {'projects':projects, 'skills':skills, 'blogs':blogs, 'educations':educations, 'experiences':experiences, 'cv':cv, 'generalSkills':generalSkills, 'yearsOfExperience':yearsOfExperience}

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        if name == '' or email == '' or subject == '' or message == '':
            return JsonResponse({"status": "error", "message": "Please fill in all fields"}, status=400)
        
        else:
            contact = Contact(name=name, email=email, subject=subject, message=message)
            contact.save()
            messages.success(request, 'Your message has been sent successfully. Thank you. I will get back to you soon.')
            return JsonResponse({"status": "success", "message": "Your message has been sent successfully. Thank you. I will get back to you soon."})

    else:

        return render(request,'portfolio/index.html', context)

def details(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    blogs = Blog.objects.all()
    context = {'blog':blog, 'blogs':blogs}
    return render(request,'portfolio/details.html', context)
