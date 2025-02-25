from django.db import models
from django.utils.text import slugify

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=105)
    last_name = models.CharField(max_length=155)
    email_address = models.EmailField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Tag(models.Model):
    name = models.CharField(max_length=55)
    caption = models.CharField(max_length=155)
    
    def __str__(self):
        return self.name



class Post(models.Model):
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name='post')
    title = models.CharField(max_length=155)
    excerpt = models.CharField(max_length=255)
    image_name = models.CharField(max_length=155)
    date = models.CharField(max_length=55)
    slug = models.SlugField(default='', unique=True, null=True)
    content = models.CharField(max_length=355)
    tag = models.ManyToManyField(Tag)

    created = models.DateTimeField(auto_now_add=True)
    last_changed = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super.save(*args, **kwargs)
    
    def __str__(self):
        return self.title
