from django.db import models



class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    # image = models.ImageField(upload_to='portfolio/images/', default='portfolio/images/None/no-img.jpg')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
    
class Skill(models.Model):
    title = models.CharField(max_length=100)
    percent = models.IntegerField()
    color = models.CharField(max_length=100)
    fade = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    # image = models.ImageField(upload_to='portfolio/images/', default='portfolio/images/None/no-img.jpg')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=250)

    def __str__(self):
        return self.name
    
class Education(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
