from django.db import models

class Product2(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    availability = models.BooleanField(default=True)
    creation_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f'{self.title} - {self.price}'


    def get_absolute_url(self):
        return f'/{self.pk}'
