from django.db import models


# Create your models here.
# model is meant by a table
    

class AddressDetailModel(models.Model):
    pincode = models.IntegerField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)


"""
father_name -> charfield
father_number -> charfield
mother_name -> charfield
mother_number -> charfield
student_number -> charfield
gmail -> charfield                                

"""


class StudentContactInfo(models.Model):
    father_name = models.CharField(max_length=100)
    father_number = models.CharField(max_length=10)
    mother_name = models.CharField(max_length=100)
    mother_number = models.CharField(max_length=10)
    student_number = models.CharField(max_length=10)
    gmail = models.EmailField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)


class AddressDetailModel(models.Model):
    pincode = models.IntegerField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    
    created_at = models.DateTimeField(auto_now_add=True)

# Name -> char
# Rollno -> int
# year_of_joining -> DateField
# Branch -> char
# year_of_joining -> DateField

class StudentDetailModel(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.IntegerField(unique=True)
    year_of_joining = models.DateField()
    branch = models.CharField(max_length=100)
    dob = models.DateField()

    # One to One Relation
    contact_info = models.OneToOneField(StudentContactInfo, on_delete=models.CASCADE,
                                        related_name="student_detail_contact_info", null=True)

    # One to Many Relation
    address = models.ForeignKey(AddressDetailModel, on_delete=models.CASCADE,
                                related_name="student_detail_address_info", null=True, blank=True)

    # This is a mandatory field in all databases
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class StudentPrevEducation(models.Model):
    student = models.ForeignKey(StudentDetailModel, on_delete=models.CASCADE,related_name="student_prev_education",null=True,blank=True)
    university = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    percentage = models.IntegerField()
    address = models.ForeignKey(AddressDetailModel, on_delete=models.CASCADE, related_name="student_prev_education_address", null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)