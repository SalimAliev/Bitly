from django.db import models


class Url(models.Model):
    objects = models.Manager()
    long_url = models.URLField(max_length=200, unique=True)
    short_url = models.CharField(max_length=10, unique=True)
    date_create = models.DateField(auto_now=True)
    requests_count = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('date_create',)

    def __str__(self):
        return self.long_url