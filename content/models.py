from django.db import models
# Create your models here.

class Content(models.Model):
    name = models.CharField(max_length=50 , unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    brand = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    description = models.TextField()
    features = models.CharField(max_length=50)
    price = models.IntegerField()   # 120.65
    colors = models.CharField(max_length=10)
    sizes = models.CharField(max_length=10)
    availability = models.BooleanField(default=False,blank=True)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    num_reviews = models.IntegerField() 
    seller_name = models.CharField(max_length=50)
    seller_rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    img = models.ImageField(upload_to='photos/content', blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    