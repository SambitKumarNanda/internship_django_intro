from django.db import models

# Create your models here.

class UserModel(models.Model):
    email = models.EmailField(max_length=50, null=True, blank=True)
    username = models.CharField(max_length=50, null=True, blank=True)
    contact = models.IntegerField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return self.username
    
    
class UserProfileModel(models.Model):
    user_info = models.OneToOneField(UserModel , on_delete=models.CASCADE, blank=True, related_name="user_profile_model_user_info")
    bio = models.CharField(max_length=200, null=True, blank=True)
    followers = models.IntegerField(null=True, blank=True)
    posts = models.IntegerField(null=True, blank=True)
    following = models.IntegerField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    # def __str__(self):
    #     return self.bio
    
    
class UserPostModel(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=150, null=True, blank=True)
    user_detail_profile = models.ForeignKey(UserProfileModel, on_delete=models.CASCADE, blank=True, null=True, related_name="user_post_model_post_info")

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    
    def __str__(self):
        return self.title
    
    
    


    


    