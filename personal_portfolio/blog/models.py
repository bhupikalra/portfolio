from django.db import models

# Create your models here.
class Category(models.Model):
    category  = models.CharField(max_length = 255)

    def __str__(self):
        return self.category

class Post(models.Model):
    title = models.CharField(max_length = 100)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add =True)
    modified_on = models.DateTimeField(auto_now = True)
    categories = models.ManyToManyField('Category', related_name = "posts")

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    author = models.CharField( max_length=100)
    body = models.TextField()
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add= True)

