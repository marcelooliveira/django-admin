from django.db import models

class Category(models.Model):
    description = models.TextField()
    
    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.description}"
