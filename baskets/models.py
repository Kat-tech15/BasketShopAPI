from django.db import models
from accounts.models import CustomUser

class Basket(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='baskets')
    name = models.CharField(max_length=100, default='Kiondo')
    image = models.ImageField(upload_to='basket_images/', null=True, blank=True)
    SIZE_CHOICES = [
        ('large','Large'),
        ('medium', 'Medium'),
        ('small', 'Small'),
    ]
    size =models.CharField(max_length=100, choices=SIZE_CHOICES, default='medium')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.size} - {self.price}"