from django.db import models


# Create your models here.
class Category(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    parent_category = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
