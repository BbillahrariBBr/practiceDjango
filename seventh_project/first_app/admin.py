from django.contrib import admin
from first_app.models import StudentModel,StudentInfoModel,TeacherInfoModel,EmployeeModels,ManagerModels

# Register your models here.

admin.site.register(StudentModel)
admin.site.register(StudentInfoModel)
admin.site.register(TeacherInfoModel)

# admin.site.register(EmployeeModels)
# admin.site.register(ManagerModels)

@admin.register(EmployeeModels)
class EmployeeModelsAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'city','designation']

@admin.register(ManagerModels)
class ManagerModelsAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'city','designation','take_interview','hiring']
