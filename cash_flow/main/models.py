from django.db import models
from smart_selects.db_fields import ChainedForeignKey
class Category(models.Model):
    name = models.CharField(max_length=64)
    type = models.ForeignKey("Type", on_delete=models.CASCADE, related_name='categories')
    def __str__(self):
        return self.name

class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    name = models.CharField(max_length=64)
    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length=64)
    def __str__(self):
        return self.name

class Status(models.Model):
    name = models.CharField(max_length=64)
    def __str__(self):
        return self.name

class Records(models.Model):
    date = models.DateTimeField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    category = ChainedForeignKey(Category, chained_field="type", chained_model_field="type",
                                 show_all=False, auto_choose=True, sort=True)
    subcategory = ChainedForeignKey (Subcategory, chained_field='category', chained_model_field='category',
                                     show_all=False, auto_choose=True, sort=True)
    cost = models.IntegerField()
    notice = models.TextField(max_length=1000)

    def __str__(self):
        return self.notice
