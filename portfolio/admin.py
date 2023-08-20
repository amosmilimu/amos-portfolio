from django.contrib import admin
from .models import Project, Skill, Blog, Education, Experience, Contact, CV, GeneralSkill

admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Blog)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Contact)
admin.site.register(CV)
admin.site.register(GeneralSkill)