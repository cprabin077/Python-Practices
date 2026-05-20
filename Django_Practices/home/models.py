from django.db import models

# Create your models here.

class User(models.Model):
    full_name = models.CharField(max_length=100, help_text="user full name")
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name
    
    class Meta:
        db_table = "user"
