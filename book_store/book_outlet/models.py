from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
# from django.utils.text import slugify

# Create your models here.


class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=55)
    city = models.CharField(max_length=55)
    
    def __str__(self):
        return f"{self.street}, {self.postal_code}, {self.city}"
    
    class Meta:
        verbose_name_plural = "Adresses"


class Author(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=105)
    # one-to-one relation
    # Author.address.street
    address = models.OneToOneField(
        Address, on_delete=models.CASCADE, null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Book(models.Model):
    title = models.CharField(max_length=55)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    # one-to-many relation
    # Author.book_set.all - related_name > Author.books.all
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name='books')
    is_best_selling = models.BooleanField(default=False)
    slug = models.SlugField(
        default='', blank=True, db_index=True)

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"
