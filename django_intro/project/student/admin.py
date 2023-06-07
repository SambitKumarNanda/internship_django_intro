from django.contrib import admin
from student.models import StudentDetailModel, StudentContactInfo, AddressDetailModel

# Register your models here.

admin.site.register(StudentDetailModel)
admin.site.register(StudentContactInfo)
admin.site.register(AddressDetailModel)
