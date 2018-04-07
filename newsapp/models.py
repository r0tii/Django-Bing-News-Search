from django.db import models

# Create your models here.
class SearchTerm(models.Model):
    term = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.term