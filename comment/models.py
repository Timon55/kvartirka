from django.db import models


class Poll(models.Model):
    name = models.CharField(max_length=255)
    details = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
