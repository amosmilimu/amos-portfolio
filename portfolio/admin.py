from django.contrib import admin
from .models import Project, Skill, Blog, Education, Experience

admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Blog)
admin.site.register(Education)
admin.site.register(Experience)