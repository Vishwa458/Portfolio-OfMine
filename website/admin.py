from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

admin.site.site_header = 'Vishwa World'

admin.site.register([WebAppDeveloper, SoftwareDevelopment, PersonalDetail, Skill, Experience])
