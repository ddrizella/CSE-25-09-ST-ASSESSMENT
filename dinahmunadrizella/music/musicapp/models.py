from django.db import models

# Create your models here.

class Song(models.Model):
    Tittle = models.CharField(max_length=255)
    Artist = models.CharField(max_length=255)
    Album = models.CharField(max_length=255, blank=True,null=True)
    Year_of_release = models.CharField(max_length=255)
    Audio_file = models.FileField(upload_to='audios/')

def __str__(self):
    return f"{self.title} - {self.artist}"


