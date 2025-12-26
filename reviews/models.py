from django.db import models
from accounts.models import CustomUser
from orders.models import Basket

class Review(models.Model):
    reviewer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reviews')
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, related_name='orders')
    rating = models.IntegerField(default=1)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.reviewer} - {self.rating}"
