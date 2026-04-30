from django.db import models
from django.utils.text import slugify
import uuid


# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    surename = models.CharField(max_length=100)
    age = models.IntegerField(blank=False)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    picture = models.ImageField(upload_to='media/', null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(f"{self.name}-{self.surename}")
            unique_id = str(uuid.uuid4())[:4]
            self.slug = f"{base_slug}-{unique_id}"
            # self.slug = slugify(f"{self.name}-{self.surename}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} {self.surename}"

