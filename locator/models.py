from django.db import models


class Locator(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    points = models.TextField()
    adjuscent = models.TextField()

    class Meta:
        ordering = ['created']