from django.db import models



class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio/images/', null=True, blank=True)
    icon = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    url = models.URLField(blank=True, null=True)
    priority = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
class Skill(models.Model):
    title = models.CharField(max_length=100)
    percent = models.IntegerField()
    color = models.CharField(max_length=100)
    fade = models.CharField(max_length=100)
    priority = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=100)
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to='portfolio/media/', default='portfolio/media/img_bg_3.jpg')
    dateCreated = models.DateTimeField(auto_now_add=True)
    url = models.URLField(blank=True)
    priority = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=250)

    def __str__(self):
        return self.name
    
class Education(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField(blank=True)
    priority = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Experience(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    fade = models.CharField(max_length=100)
    priority = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
class CV(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
    

class GeneralSkill(models.Model):
    title = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    fade = models.CharField(max_length=100)
    priority = models.IntegerField(default=0)

    def __str__(self):
        return self.title