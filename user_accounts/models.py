from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Account(models.Model):
    """
    Model for user accout/profile
    """
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=6)
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    phone = models.CharField(max_length=12)
    postcode = models.CharField(max_length=6)
    street_address = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_profile_dwzcuabfl'
    )

    class Meta:
        ordering = ['-created_at']
    
    def __str__ (self):
        return f"{self.owner}'s account"
    
    def create_account(sender, instance, created, **kwargs):
        if created:
            Account.objects.create(owner=instance)
    
    post_save.connect(create_account, sender=User)
