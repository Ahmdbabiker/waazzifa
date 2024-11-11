from django.contrib import admin
from .models import *

# Registering other models
admin.site.register(Category)
admin.site.register(Comment)

@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}

admin.site.register(Emails)
admin.site.register(EmailCat)
admin.site.register(Advertisement)
admin.site.register(Service)
admin.site.register(Sendmessage)

# Define an inline for Education model
class EducationInline(admin.TabularInline):
    model = Education
    extra = 1  # Number of empty forms to display for new entries
    fields = ('education', 'education_name', 'end_edu_date')  # Fields to display in the inline

# Define an inline for WorkExperience model
class WorkExperienceInline(admin.TabularInline):
    model = WorkExperience
    extra = 1
    fields = ('company_name', 'position', 'start_date', 'end_date', 'description')

# Define an inline for Certificate model
class CertificateInline(admin.TabularInline):
    model = Certificate
    extra = 1
    fields = ('certificate',)

# Customizing the CVorders model in the admin panel
@admin.register(CVorders)
class CVordersAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('fullname', 'job_title', 'phone', 'email', 'dof', 'address', 'likndein', 'skill', 'langugaes')
    
    # Fields to make searchable in the admin interface
    search_fields = ('fullname', 'job_title', 'email', 'phone')
    
    # Fields to filter by in the admin interface
    list_filter = ('job_title', 'dof')

    # Fields to display in the form view (optional if you want to control the form fields in admin)
    fields = ('fullname', 'job_title', 'phone', 'email', 'dof', 'address', 'likndein', 'skill', 'langugaes')
    
    # Adding the inlines to display related data
    inlines = [EducationInline, WorkExperienceInline, CertificateInline]

# No need to register CVorders again
