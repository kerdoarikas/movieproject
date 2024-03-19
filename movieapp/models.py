from django.db import models

class Country(models.Model):
    common = models.CharField(max_length=80)
    official = models.CharField(max_length=80)
    capital = models.CharField(max_length=80)
    region = models.CharField(max_length=80)
    subregion = models.CharField(max_length=80, null=True, blank=True)
    flag = models.CharField(max_length=250)
    maps = models.CharField(max_length=250)

    class Meta:
        ordering = ["common"]
        verbose_name_plural = "countries"

    def __str__(self):
        return self.common


class Movie(models.Model):
    title = models.CharField(max_length=100)
    year = models.CharField(max_length=20)
    imdbid = models.CharField(max_length=30)
    type = models.CharField(max_length=20)
    poster = models.CharField(max_length=150, null=True, blank=True)

    class Meta:
        ordering = ["title"]
        verbose_name_plural = "movies"

    def __str__(self):
        return self.title
