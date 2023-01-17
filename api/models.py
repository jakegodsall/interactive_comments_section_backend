from django.db import models

# Create your models here.


class ProfileImage(models.Model):
    png_image = models.ImageField()
    webp_image = models.ImageField()


class Profile(models.Model):
    username = models.CharField(max_length=30, blank=False)
    name = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=False)
    images = models.ForeignKey(ProfileImage, on_delete=models.CASCADE)


class Message(models.Model):
    content = models.TextField(max_length=1000, blank=False)
    profile = models.OneToOneField(
        Profile, on_delete=models.CASCADE, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(default=0)
