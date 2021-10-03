from django.db import models

# Create your models here.
class AddBlog(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField(max_length=100000)
    genre = models.CharField(max_length=100) #make dropdown with option to add custom value
    author = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + ' by ' + self.author


        
