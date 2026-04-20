from django.db import models

class Entry(models.Model):
    CATEGORY_CHOICES = [
        ('trainer', 'Trainer'),
        ('student', 'Student'),
        ('patient', 'Patient'),
        ('product', 'Product'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='student')
    rating = models.PositiveSmallIntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name