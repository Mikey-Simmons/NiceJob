from django.db import models
import re 
class UserManager(models.Manager):
    def basic_validator(self,postData):
        errors = {}
        if len(postData['first_name']) < 3:
            errors['first_name'] = "First name needs to be at least 3 characters"
        if len(postData['last_name']) < 3:
            errors['last_name'] = "Last name needs to be at least 3 characters"
        if len(postData['email']) < 8:
            errors['email'] = "Email needs to be at least 8 characters"
        if len(postData['password']) < 8:
            errors['password'] = "Password needs to be at least 8 characters"
        if postData['password'] != postData['confirm_password']:
            errors['invalid_password'] ="Passwords do not match!"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        return errors
    def login_validator(self,postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    
            errors['email'] = "Invalid email address!"
        if len(postData['email']) < 8:
            errors['email'] = "Email needs to be at least 8 characters"
        return errors
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Job(models.Model):
    company = models.CharField(max_length=255, default="not-listed")
    title = models.CharField(max_length=255)
    date_applied = models.DateField()
    applied_on = models.CharField(max_length=100
    )
    location = models.CharField(max_length=255)
    website = models.CharField(max_length=300)
    next_steps = models.CharField(max_length=300)
    comments = models.TextField()
    rejected = models.BooleanField(default=False)
    uploaded_by = models.ForeignKey(User, related_name="jobs_uploaded",on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    