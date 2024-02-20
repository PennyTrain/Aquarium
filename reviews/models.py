from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

STATUS = ((0, "Draft"), (1, "Posted"))


class ReviewPost(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=400, unique=True, blank=True)
    author = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE, related_name="review_post")
    content = models.TextField(max_length=10000)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)
    featured_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('ReviewPostDisplay')
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(ReviewPost, self).save(*args, **kwargs)
    

    
    
