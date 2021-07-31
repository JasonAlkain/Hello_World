from django.db import models

# Mr, Mrs, Ms,

PREFIX_CHOICES = {
    ('Mr', 'Mr'),
    ('Mrs', 'Mrs'),
    ('Ms', 'Ms'),
}

class Profile(models.Model):
    prefixes = models.CharField(max_length=60, choices=PREFIX_CHOICES, default='')
    first_name = models.CharField(max_length=60, default='', blank=True, null=False)
    last_name = models.CharField(max_length=60, default='', blank=True, null=False)
    email = models.CharField(max_length=128, default='', blank=True, null=False)
    username = models.CharField(max_length=60, default='', blank=True, null=False)

    objects = models.Manager()


    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)