from django.conf import settings
from django.db import models
import random, string


class Santa(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    santa_group = models.ForeignKey(
        'secretsanta.SantaGroup',
        on_delete=models.CASCADE,
        related_name='santas')

    def __str__(self):
        return self.user.username


class SantaGroup(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20)
    joinable = models.BooleanField(default=True)
    description = models.TextField()
    distribution_date = models.DateTimeField(blank=True, null=True)
    admin = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def generate_code(self):
        self.code = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=15))
