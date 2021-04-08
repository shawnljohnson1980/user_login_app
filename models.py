from django.db import models
import re


class UserManager(models.Manager):

    def basic_validator(self, post_data):
        errors = {}
        email_regex = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not email_regex.match(post_data['email']):
            errors['email_pattern'] = "Email Address is Invaild Please provide name@domain.com"
        if post_data['email']==['email']:
            errors ['email_unique']

        elif len(post_data['password']) < 8:
            errors['password_length'] = 'Password must be between 8 and 60 characters in length'
        if post_data['password'] != post_data['confirm_password']:
            errors['password_match'] = "passwords must match.."

        if len(post_data['first_name']) < 5 or len(post_data['first_name']) > 45:
            errors['first_name_length'] = 'first name should be at least 5 characters long, and no loger than 45 characters in length.'

        if len(post_data['last_name']) < 5 or len(post_data['last_name']) > 45:
            errors['last_name_length'] = 'last name should be at least 5 characters long, and no loger than 45 characters in length.'
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=60)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = UserManager()
