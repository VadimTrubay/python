
from django.db import models


class Price(models.Model):
    title = models.CharField(max_length=50, null=False)
    gas = models.FloatField(null=False)
    dp = models.FloatField(null=False)
    nf = models.FloatField(null=False)
    nf_plus = models.FloatField(null=False)
    nt = models.FloatField(null=False)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'



