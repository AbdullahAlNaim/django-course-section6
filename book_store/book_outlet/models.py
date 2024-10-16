from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=2)  

    def country_name(self):
        return self.name

    def __str__(self):
        return self.country_name()

    class Meta:
        verbose_name_plural = 'Countries'

class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)

    def full_address(self):
        return f'{self.street}, {self.city}, {self.postal_code}'

    def __str__(self):
        return self.full_address()

    # this is to modify how models are shown/spelled in admin view
    class Meta:
        verbose_name_plural = "Address Entries"

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()
    

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    # related_name lets us query the model relationship using that name instead name_set instead
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name="books")
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default='', blank=True,null=False, db_index=True)
    published_countries = models.ManyToManyField(Country)

    def get_absolute_url(self):
        return reverse('chosen-book', args=[self.slug])  

    # removed this since admin side can create the slug part
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.rating}) {self.author} {self.is_bestselling}"
