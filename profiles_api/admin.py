from django.contrib import admin
from profiles_api import models


""" register user profile model to admin site"""
admin.site.register(models.User_Profile)
admin.site.register(models.ProfileFeedItem)
