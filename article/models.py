from django.db import models

# Create your models here.
class Article(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)

    def __str__(self):
        return "%d : (%s)"%(self.id, self.title)
