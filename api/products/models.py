from django.db import models
from rest_framework import serializers



class Product(models.Model):
    title = models.CharField('Title',max_length=120)
    description = models.TextField('Description',null=True)
    price = models.IntegerField('Price')

    def __str__(self):
        return self.title

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'    