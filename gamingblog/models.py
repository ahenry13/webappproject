from django.db import models

# Create your models here.
class Games(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def _unicode_(self):
        return self.name

class Blog(models.Model):
    category = models.ForeignKey(Games)
    title = models.CharField(max_length=128)

    def _unicode_(self):
        return self.title
