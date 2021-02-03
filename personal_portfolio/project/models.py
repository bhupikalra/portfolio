from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField(blank = True)
    technology = models.CharField(max_length = 20)
    image = models.ImageField(upload_to = "media/project_images/%Y/%m/")
    created_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title
