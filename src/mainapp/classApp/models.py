from django.db import models

# Create your models here.


class ClassApp(models.Model):
    # Title of the class
    title = models.CharField(
        max_length=9000, default='', blank=False, null=False)
    # Course Number
    course_number = models.IntegerField(
        max_length=60, default=0, blank=False, null=False)
    # Instructor Name
    instructor_name = models.CharField(
        max_length=128, default='', blank=False, null=False)
    # Duration of the Class in hours
    duration = models.DecimalField(
        max_digits=4, decimal_places=1, default=0.0, blank=False, null=False)
    # Add the models manager
    objects = models.Manager()

    # Returns a more comprehensive name
    def __str__(self):
        return '{} | {} | {}'.format(self.course_number, self.title, self.duration)
