from django.db import models
from shortuuid.django_fields import ShortUUIDField
# Create your models here.
class ItemModel(models.Model):
    item_id = ShortUUIDField(
        length=6, max_length=6, alphabet="0123456789", primary_key=True
    )
    item_name = models.CharField(max_length=30,unique=True)
    item_quantity = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.item_id} - {self.item_name}"