from django.db import models
from django.utils.text import slugify
from django.core.validators import MinLengthValidator

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=105)
    last_name = models.CharField(max_length=155)
    email_address = models.EmailField(null=True, blank=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Tag(models.Model):
    name = models.CharField(max_length=55)
    caption = models.CharField(max_length=155)
    
    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL,
        null=True, related_name='post')
    title = models.CharField(max_length=155)
    excerpt = models.CharField(max_length=255)
    image = models.ImageField(upload_to='posts', null=True)
    date = models.DateField()
    # db_index=True by default
    slug = models.SlugField(default='', unique=True, blank=True)  
    content = models.TextField(validators=[MinLengthValidator(25)])
    tags = models.ManyToManyField(Tag)

    created = models.DateTimeField(auto_now_add=True)
    last_changed = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, null=True, related_name="authors")
    user_name = models.CharField(max_length=105)
    user_email = models.EmailField()
    text = models.TextField(max_length=355)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
