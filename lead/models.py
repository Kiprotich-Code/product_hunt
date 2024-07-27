from django.db import models
from accounts.models import CustomUser

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()

    def __str__(self):
        return self.name
    

class Product(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=250)
    desc = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} by {self.author}'
    

class Vote(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    vote_type = models.CharField(max_length=10, choices=[('upvote', 'Upvote'), ('downvote', 'Downvote')])

    class Meta:
        unique_together = ('user', 'product')


class Contact(models.Model):
    email = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return f'Message from {self.email}'
