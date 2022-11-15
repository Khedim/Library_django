from django.db import models

# Create your models here.

class Category(models.Model):
  name = models.CharField(max_length=255)
  def __str__(self):
    return self.name

class Book(models.Model):
  status_book = [
    ('availbe', 'availbe'),
    ('renatl', 'renatl'),
    ('sold', 'sold'),
  ]

  title = models.CharField(max_length=255)
  author = models.CharField(max_length=255, null=True, blank=True)
  photo_book = models.ImageField(upload_to='photos', null=True, blank=True)
  photo_author = models.ImageField(upload_to='photos', null=True, blank=True)
  pages = models.IntegerField(null=True, blank=True)
  price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
  retal_price_day = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
  retal_period = models.IntegerField(null=True, blank=True)
  retal_total = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
  active = models.BooleanField(default=True)
  status = models.CharField(max_length=50, choices=status_book, null=True, blank=True)
  category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True)
  def __str__(self):
    return self.title






  # in case you dont have images in database
  # def get_photo_author_url(self):
  #   if self.photo_author and hasattr(self.photo_author, 'url'):
  #       return self.photo_author.url
  # def get_photo_book_url(self):
  #   if self.photo_book and hasattr(self.photo_book, 'url'):
  #       return self.photo_book.url
