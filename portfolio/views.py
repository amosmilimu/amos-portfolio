from django.shortcuts import render, redirect
from .models import Project, Skill, Blog, Education, Experience, Contact, CV

# Create your views here.

def index(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    blogs = Blog.objects.all()
    educations = Education.objects.all()
    experiences = Experience.objects.all()
    if CV.objects.all():
        cv = CV.objects.all()[0]
    else:
        cv = None
    context = {'projects':projects, 'skills':skills, 'blogs':blogs, 'educations':educations, 'experiences':experiences, 'cv':cv}

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        if name == '' or email == '' or subject == '' or message == '':
            context['error'] = 'Please fill in all fields'
        
        else:
            contact = Contact(name=name, email=email, subject=subject, message=message)
            contact.save()
            context['success'] = 'Your message has been sent successfully thank you. I will get back to you soon.'
        return redirect('index')

    else:

        return render(request,'portfolio/index.html', context)

def details(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    blogs = Blog.objects.all()
    context = {'blog':blog, 'blogs':blogs}
    return render(request,'portfolio/details.html', context)
